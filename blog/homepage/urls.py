from django.urls import path

from homepage.views import GetAllPostView

urlpatterns = [
    path('posts/', GetAllPostView.as_view()),
]
