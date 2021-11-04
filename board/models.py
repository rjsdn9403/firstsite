from django.db import models
from acc.models import User

# Create your models here.
class Board(models.Model):
    subject = models.CharField(max_length=100)
    writer = models.CharField(max_length=50)
    content = models.TextField()
    ctime = models.DateTimeField()
    up = models.ManyToManyField(User, blank=True)

    def summary(self):
        if len(self.content) >= 40:
            return self.content[:30] + "..."
        return self.content

class Reply(models.Model):
    sub = models.ForeignKey(Board, on_delete=models.CASCADE)
    replyer = models.CharField(max_length=50)
    comment = models.TextField()