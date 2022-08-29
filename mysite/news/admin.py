from django.contrib import admin

# Register your models here.
from .models import News, Category

admin.site.register(News)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'creared_at', 'udpated_at', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)

admin.site.unregister(News)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)

