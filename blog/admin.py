from django.contrib import admin

from .forms import PostForm
from .models import Post, Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostForm
    # ... other admin settings ...

admin.site.register(Category)
