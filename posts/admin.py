from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

# Register your models here.
admin.site.register(Post, PostAdmin)