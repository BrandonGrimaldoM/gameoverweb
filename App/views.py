from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

from App.forms import PostForm
from App.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    template_name = 'App/index.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 5
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'App/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    template_name = 'App/new.hTml'
    form_class = PostForm
    success_url = reverse_lazy('App:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
