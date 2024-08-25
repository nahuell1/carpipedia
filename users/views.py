from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .models import User
from posts.models import Post
from .forms import UserForm

# Create your views here.

# class deleteAccountMDL(UpdateView):
#    template_name = "accounts/login.html"


class UsrDetailView(DetailView):
    template = 'usr_detail.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(
            propietario=self.get_object()).order_by('-fecha_creacion')
        return context


class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    success_message = 'El perfil se actualizó correctamente!'
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return f'/accounts/detalle/{self.get_object().pk}'


class UserDeleteView(DeleteView):
    model = User()
    success_url = "/"

    def get_object(self, queryset=None):
        return self.request.user
