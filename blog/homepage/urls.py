from django.urls import path

from homepage.views import GetAllPostsView

urlpatterns = [
    path('posts/', GetAllPostsView.as_view()),
]
