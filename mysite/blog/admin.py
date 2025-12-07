from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configuración del panel de administración para el modelo Post.
    """
    list_display = ('title', 'author', 'published', 'created_at', 'updated_at')
    list_filter = ('published', 'author', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
