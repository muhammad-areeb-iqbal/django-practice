from django.contrib import admin
from .models import Post2Model

class Post2ModelAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'slug',
        'content',
        'publish',
        'view_count',
        'publish_date',
        'author_email',
        'updated',
        'timestamp',
        'get_age'
    ]
    readonly_fields = ['slug', 'updated', 'timestamp', 'get_age']

    def get_age(self, obj, *args, **kwargs):
        return "Empty"

    class Meta:
        model = Post2Model

# Register your models here.
admin.site.register(Post2Model, Post2ModelAdmin)