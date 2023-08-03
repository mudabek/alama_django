from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # import User model django created
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # if uses is deleted we want to delete its posts
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    # videos = models.ManyToManyField('Video', related_name='courses')

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('course-detail', kwargs={'pk': self.pk})


# class Video(models.Model):
#     video_id = models.CharField(max_length=20)
#     title = models.CharField(max_length=255)