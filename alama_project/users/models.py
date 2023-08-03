from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from courses.models import Course

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    courses_purchased = models.ManyToManyField(Course, blank=True, related_name='purchased_by')


    def __str__(self):
        return f'{self.user.username} Profile'

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


    def has_purchased_course(self, course):
        return self.courses_purchased.filter(pk=course.pk).exists()