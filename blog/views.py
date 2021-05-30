from django.shortcuts import render
from django.contrib.auth.mixins import *
from django.views.generic import *
from .models import Post


# default template name for class based view: <app-name>/<model-name>_<view-type>.html

# home page
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


# def home(request):
#     context = {'posts': Post.objects.all()}
#     return render(request, 'blog/home.html', context)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)
