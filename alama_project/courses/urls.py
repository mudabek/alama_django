from django.urls import path
from .views import (
    CourseListView, 
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    UserCourseListView,
    CoursePurchaseView
)
from . import views

urlpatterns = [
    path('', CourseListView.as_view(), name='courses-home'),
    path('user/<str:username>', UserCourseListView.as_view(), name='user-courses'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('course/new/', CourseCreateView.as_view(), name='course-create'),
    path('course/<int:pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('course/<int:pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('course/<int:pk>/purchase/', CoursePurchaseView.as_view(), name='course-purchase'),
    path('about', views.about, name='courses-about'),
]