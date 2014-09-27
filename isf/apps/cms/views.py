from django.views.generic import ListView, DetailView
from cms.models import Post


class PostList(ListView):
    """
    """
    queryset = Post.objects.filter(is_active=True)
    template_name = 'post_list.html'


class PostDetail(DetailView):
    """
    """
    model = Post
    template_name = 'post_detail.html'
