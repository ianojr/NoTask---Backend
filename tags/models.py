from django.db import models
from django.contrib.auth.models import User
from notes.models import Notes
from tasks.models import Tasks

# Create your models here.
class Tags(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    color = models.CharField(default='black')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class NoteTags(models.Model):
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class TaskTags(models.Model):
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class NoteTasks(models.Model):
    notes = models.ForeignKey(Notes, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)