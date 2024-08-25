from django.db import models
from django.utils.text import slugify
from users.models import User
from tinymce import models as tinymce_models


class Categoria(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.titulo


class Post(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    contenido = tinymce_models.HTMLField()
    fecha_creacion = models.DateField(auto_now_add=True, db_index=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(User,
                                      related_name="dislikes",
                                      blank=True)
    categorias = models.ManyToManyField(Categoria, blank=True)

    def __str__(self):
        return self.titulo

    @property
    def total_likes(self):
        return self.likes.count()

    @property
    def total_dislikes(self):
        return self.dislikes.count()

    @property
    def media_like_dislike(self):
        return self.total_likes - self.total_dislikes

    def save(self, *args, **kwargs):
        slug = slugify(self.titulo)
        super().save(*args, **kwargs)
