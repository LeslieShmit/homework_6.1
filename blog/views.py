from .models import Blog

from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'Blog/home.html'
    ordering = ['-created_at']
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_published=True)


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'Blog/blog_form.html'
    fields = ['title', 'content', 'image', 'is_published',]
    success_url = reverse_lazy('blog:home')


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_details.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()

        if self.object.views_counter == 100:
            send_mail(
                subject='Поздравляем!',
                message=f'Статья "{self.object.title}" достигла 100 просмотров!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['email@example.com'],
                fail_silently=False,
            )
        return self.object


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'content', 'image', 'is_published',]
    template_name = 'Blog/blog_form.html'
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.change_blog'

    def get_success_url(self):
        return reverse('blog:blog_details', args=[self.kwargs.get('pk')])



class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    template_name = 'Blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog:home')
    permission_required = 'blog.delete_blog'
