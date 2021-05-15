"""Posts views."""

# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

# Forms
from App.forms import PostForm

# Models
from App.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'App/index.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 5
    context_object_name = 'posts'


class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'App/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'App/new.hTml'
    form_class = PostForm
    success_url = reverse_lazy('App:index')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context
