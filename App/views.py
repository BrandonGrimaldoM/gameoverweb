from django.shortcuts import render
from django.views.generic import DetailView
# Create your views here.
class PostsFeedView(DetailView):
    
    def index(request):
      return render(request, 'App/index.html')