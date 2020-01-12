from django.urls import path
from . import views

urlpatterns = [
    path('',views.postlist,name='postlist'),  # post list is name of url(uniform resource locator) used to find out the view
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # pk stands for primary key 
    # for example https://127.0.0.8000/post/5/ post/ means user is looking for view named post details and 5 means int:pk primary key like post number 5 
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('blog/register',views.register,name='register'),
]