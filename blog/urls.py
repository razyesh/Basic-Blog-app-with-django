from django.urls import path
from .views import  DetailView, PostCreateView
from . import views
urlpatterns = [
    path('', views.post_list, name = 'postlist'),
    path('<slug:slug>', DetailView.as_view(), name = 'detailview'),
    path('post/new', PostCreateView.as_view(), name="post-create" ),
]