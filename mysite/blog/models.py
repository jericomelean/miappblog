from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    """
    Representa una entrada de blog.
    """
    title = models.CharField(max_length=200, unique=True, help_text="El título de la entrada del blog.")
    slug = models.SlugField(max_length=200, unique=True, blank=True, help_text="Una URL amigable para la entrada.")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', help_text="El autor de la entrada.")
    content = models.TextField(help_text="El contenido principal de la entrada.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="La fecha y hora en que se creó la entrada.")
    updated_at = models.DateTimeField(auto_now=True, help_text="La fecha y hora de la última actualización de la entrada.")
    published = models.BooleanField(default=False, help_text="Indica si la entrada es visible para el público.")

    def save(self, *args, **kwargs):
        """
        Sobrescribe el método de guardado predeterminado para generar automáticamente un slug si no se proporciona uno.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        """
        Devuelve una representación de cadena de la entrada, que es su título.
        """
        return self.title

    class Meta:
        """
        Opciones de metadatos para el modelo Post.
        """
        ordering = ['-created_at']
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
