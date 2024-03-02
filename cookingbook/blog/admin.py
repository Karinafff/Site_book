from django.contrib import admin

# Register your models here.

from .models import Post,PostPoint,Comment
admin.site.register(Post)
admin.site.register(PostPoint)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','post','created','active')
    list_filter =  ('active','created','updated')
    search_fields = ('name','email','body')