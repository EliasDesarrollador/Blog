
from django.urls import path 
from . import views
urlpatterns = [
    path ('', views.home, name='posts-home'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('posts/new/', views.post_create, name='post-create'),
]   