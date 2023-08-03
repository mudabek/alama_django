from django.views.generic import (
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Lecture
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from courses.models import Course
from django.contrib import messages


class LectureDetailView(DetailView):
    model = Lecture

    def get_object(self, queryset=None):
        lecture = super().get_object(queryset=queryset)
        course = lecture.course

        if not self.request.user.is_authenticated:
            messages.warning(self.request, "Dars ko'rish uchun kursni so'tib oling.")
            return course

        if not self.request.user.profile.has_purchased_course(course) and self.request.user != course.author:
            messages.warning(self.request, "Dars ko'rish uchun kursni so'tib oling.")
            return course
        return lecture


class LectureCreateView(LoginRequiredMixin, CreateView):
    model = Lecture
    fields = ['title', 'description', 'youtube_id']
    
    def form_valid(self, form):
        course_id = self.kwargs['pk']
        course = get_object_or_404(Course, pk=course_id)
        form.instance.course = course

        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('course-detail', kwargs={'pk': self.kwargs['pk']})
    

class LectureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Lecture
    fields = ['title', 'description', 'youtube_id']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        lecture = self.get_object()
        if self.request.user == lecture.course.author:
            return True
        return False
    
    def get_success_url(self):
        return reverse('lecture-detail', kwargs={'pk': self.object.id})
    

class LectureDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Lecture

    def test_func(self):
        lecture = self.get_object()
        if self.request.user == lecture.course.author:
            return True
        return False
    
    def get_success_url(self):
        return reverse('course-detail', kwargs={'pk': self.object.course.id})