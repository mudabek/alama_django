from django.db import models
from django.utils import timezone
from courses.models import Course

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    youtube_id = models.CharField(max_length=20)
    
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lectures'
    )

    def __str__(self):
        return self.title