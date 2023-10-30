
from django.urls import path
from .views import PostListView, PostCreateView, PostDetailViewAPI

urlpatterns = [
    path('post-list/', PostListView.as_view()),
    path('post-create/', PostCreateView.as_view()),
    path('post/<int:pk>/', PostDetailViewAPI.as_view()),

]
