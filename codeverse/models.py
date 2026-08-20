from django.db import models
from django.contrib.auth.models import User


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Topic(TimeStampedModel):
    name = models.CharField(max_length=100)
    year = models.IntegerField(default=1)
    order = models.IntegerField(default=1)
    description = models.TextField(default="")
    not_to_do = models.TextField(default="")
    key_topics = models.TextField(default="", blank=True)
    why_it_matters = models.TextField(default="", blank=True)
    code_example = models.TextField(default="", blank=True)

    def __str__(self):
        return self.name


class Progress(TimeStampedModel):
    STATUS_CHOICES = [
        ('not_started', 'Not Started'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not_started')

    class Meta:
        unique_together = ('user', 'topic')

    def __str__(self):
        return f"{self.user.username} - {self.topic.name} - {self.status}"