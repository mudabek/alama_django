from typing import Any, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django import forms
from django.views.generic import (
    View,
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Course
from .forms import CoursePurchaseForm


def home(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/home.html', context) # now context will be available within html


class CourseListView(ListView):
    model = Course
    template_name = 'courses/home.html'
    context_object_name = 'courses'
    ordering = ['-date_posted']
    paginate_by = 5


class UserCourseListView(ListView):
    model = Course
    template_name = 'courses/user_courses.html'
    context_object_name = 'courses'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Course.objects.filter(author=user).order_by('-date_posted')
        

class CourseDetailView(DetailView):
    model = Course


@method_decorator(login_required, name='dispatch')
class CoursePurchaseView(View):
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs['pk'])
        form = CoursePurchaseForm()
        return render(request, 'courses/course_purchase_form.html', {'form': form, 'course': course})

    def post(self, request, *args, **kwargs):
        course = get_object_or_404(Course, pk=self.kwargs['pk'])
        form = CoursePurchaseForm(request.POST)
        if form.is_valid():
            request.user.profile.courses_purchased.add(course)

            return redirect('course-detail', pk=course.pk)

        return render(request, 'courses/course_purchase_form.html', {'form': form, 'course': course})


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'description', 'price']

    widgets = {
            'price': forms.NumberInput(),
        }
    
    def form_valid(self, form):
        form.instance.author = self.request.user

        # Custom validation for the 'price' field
        price = form.cleaned_data['price']
        if price < 0:
            form.add_error('price', 'Price must be a positive value.')
            return self.form_invalid(form)
        
        return super().form_valid(form)
    

class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Course
    fields = ['title', 'description', 'price']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Course
    success_url = '/' # redirects home after delete

    def test_func(self):
        course = self.get_object()
        if self.request.user == course.author:
            return True
        return False


def about(request):
    return render(request, 'courses/about.html', {'title': 'Alama'})