from .models import Blog

from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'Blog/home.html'
    ordering = ['-created_at']
    paginate_by = 5


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'Blog/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published',]
    success_url = reverse_lazy('blog:home')


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_details.html'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published',]
    template_name = 'Blog/blog_form.html'
    success_url = reverse_lazy('blog:home')


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'Blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:home')
