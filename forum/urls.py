from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('<int:post_id>/', views.single_post, name='single_post'),
]
