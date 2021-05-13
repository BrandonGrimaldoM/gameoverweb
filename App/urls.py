"""Posts URLs."""

# Django
from django.urls import path

# Views
from App import views

urlpatterns = [

    path(
        route='',
        view=views.PostsFeedView.index,
        name='index'
    ),

    
]