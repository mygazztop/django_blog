from django.contrib import admin
from django_blog.apps.my_blog.models import Post, KeyWord, Author


class PostAdmin(admin.ModelAdmin):
    search_fields = ['post_title', 'post_annotation']
    list_filter = ['id']


admin.site.register(Author, admin.ModelAdmin)
admin.site.register(Post, admin.ModelAdmin)
admin.site.register(KeyWord, admin.ModelAdmin)

