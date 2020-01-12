from django.contrib import admin
from .models import Post,Comment
# Register your models here.
admin.site.register(Post) # to make our model visible to admin page we need to register it in the admin
admin.site.register(Comment)