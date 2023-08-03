from django.urls import path
from .views import (
    LectureDetailView,
    LectureCreateView,
    LectureUpdateView,
    LectureDeleteView
)

urlpatterns = [
    path('lecture/<int:pk>/', LectureDetailView.as_view(), name='lecture-detail'),
    path('lecture/new/<int:pk>', LectureCreateView.as_view(), name='lecture-create'),
    path('lecture/<int:pk>/update/', LectureUpdateView.as_view(), name='lecture-update'),
    path('lecture/<int:pk>/delete/', LectureDeleteView.as_view(), name='lecture-delete'),
]