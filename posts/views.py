from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import *
from .models import Post
from django.utils.text import slugify
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string


class PostDetailView(DetailView):
    template = 'post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return '/'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.propietario = self.request.user
        form.instance.slug = slugify(form.instance.titulo)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    paginate_by = 5


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"


class PostUpdateView(SuccessMessageMixin, UpdateView):
    model = Post
    success_message = 'El post se actualizó correctamente!'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'slug': self.object.slug})


def like_post(request):
    post = get_object_or_404(Post, slug=request.POST.get('slug'))
    is_liked = False
    is_disliked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
        is_disliked = False
    else:
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
            is_disliked = False
        post.likes.add(request.user)
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'is_disliked': is_disliked,
    }
    if request.is_ajax():
        html = render_to_string('posts/like_section.html',
                                context,
                                request=request)
        return JsonResponse({'form': html})


def dislike_post(request):
    post = get_object_or_404(Post, slug=request.POST.get('slug'))
    is_disliked = False
    is_liked = False
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        is_disliked = False
        is_liked = False
    else:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            is_liked = False
        post.dislikes.add(request.user)
        is_disliked = True
    context = {
        'post': post,
        'is_disliked': is_disliked,
        'is_liked': is_liked,
    }
    if request.is_ajax():
        html = render_to_string('posts/like_section.html',
                                context,
                                request=request)
        return JsonResponse({'form': html})