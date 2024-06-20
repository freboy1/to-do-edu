from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=150)
    done = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
    