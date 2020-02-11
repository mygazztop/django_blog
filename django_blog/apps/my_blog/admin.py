from django.contrib import admin
from django_blog.apps.my_blog.models import Post, KeyWord


admin.site.register(Post, admin.ModelAdmin)
admin.site.register(KeyWord, admin.ModelAdmin)

