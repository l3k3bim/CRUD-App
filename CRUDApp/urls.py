from django.urls import path
from .views import (
  BlogListView, 
  BlogDetailView, 
  BlogCreateView, 
  BlogUpdateView,
  BlogDeleteView
  )


urlpatterns = [
  path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete.html'),
  path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit.html'),
  path('post/new/', BlogCreateView.as_view(), name='post_new.html'),
  path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail.html'),
  path('', BlogListView.as_view(), name='home'),
]