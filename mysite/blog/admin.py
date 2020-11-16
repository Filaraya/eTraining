from django.contrib import admin
from .models import Post, Topic, Subtopic
#admin.site.register(Post)

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Topic)
class TopicAdmin (admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register (Subtopic)
class Subtopic(admin.ModelAdmin):
    list_display = ['title', 'topic','created']
    list_filter = ['created','topic']
    search_fields = ['title','details']
    prepopulated_fields = {'slug': ('title',)}




