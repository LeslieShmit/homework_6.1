from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.core.exceptions import PermissionDenied

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:home')

class EditUserView(LoginRequiredMixin, UpdateView):
    template_name = 'users/update.html'
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        # Дополнительно проверяем, что редактируемый объект — это текущий пользователь
        if form.instance != self.request.user:
            raise PermissionDenied("Вы не можете редактировать другого пользователя")
        return super().form_valid(form)