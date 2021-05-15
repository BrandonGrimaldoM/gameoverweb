from django.urls import path
from App import views

urlpatterns = [

    path(
        route='',
        view=views.PostsFeedView.as_view(),
        name='index'
    ),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'
    ),

    path(
        route='posts/<int:pk>/',
        view=views.PostDetailView.as_view(),
        name='detail'
    )
]
