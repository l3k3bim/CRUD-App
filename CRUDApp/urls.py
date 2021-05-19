from django.urls import path
from .views import BlogDeleteView, BlogUpdateView, BlogCreateView, BlogDetailView, BlogListView, signup_request, login_request, logout_request, password_reset_request, add_comment_to_post

#app_name = "CRUDApp"
urlpatterns = [
  path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete.html'),
  path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit.html'),
  path('post/new/', BlogCreateView.as_view(), name='post_new.html'),
  path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail.html'),
  path('', BlogListView.as_view(), name='home'),
  path('post/<int:pk>/comment/', add_comment_to_post, name='add_comment_to_post'),
  path("signup", signup_request, name="signup.html"),
  path("login", login_request, name="login.html"),
  path("logout", logout_request, name= "logout"),
  path("password_reset", password_reset_request, name="password_reset.html")
]