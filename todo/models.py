from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=50, null=True)
    details = models.TextField(max_length=100, blank=True, null=True)
    completed = models.BooleanField(default=False, null=True)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
        # +self.people


class Feedback(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='feedback')
    email = models.EmailField()
    feeds = models.TextField(null=True)

    def __str__(self):
        return self.user.username + " --"+self.feeds[:10]
