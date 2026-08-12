from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Topic, Progress


def home(request):
    if request.user.is_authenticated:
        progress_map = {
            p.topic_id: p.status
            for p in Progress.objects.filter(user=request.user)
        }
    else:
        progress_map = {}

    year1_topics = list(Topic.objects.filter(year=1).order_by('order'))
    year2_topics = list(Topic.objects.filter(year=2).order_by('order'))
    year3_topics = list(Topic.objects.filter(year=3).order_by('order'))

    for topic_list in (year1_topics, year2_topics, year3_topics):
        for topic in topic_list:
            topic.status = progress_map.get(topic.id, 'not_started')

    return render(request, 'codeverse/home.html', {
        'year1_topics': year1_topics,
        'year2_topics': year2_topics,
        'year3_topics': year3_topics,
    })


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


# NEW — updates a topic's progress status for the logged-in user
def update_status(request, topic_id):
    if request.method == 'POST':
        topic = get_object_or_404(Topic, id=topic_id)
        progress, created = Progress.objects.get_or_create(
            user=request.user, topic=topic
        )
        new_status = request.POST.get('status')
        if new_status in ('not_started', 'in_progress', 'completed'):
            progress.status = new_status
            progress.save()
    return redirect('home')