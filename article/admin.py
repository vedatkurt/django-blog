from django.contrib import admin

# Register your models here.

from .models import Article, Comment

def make_published(modeladmin,request,queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected Article as published"

admin.site.register(Comment)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title","author","created_date","status"]
    
    list_display_links = ["title","author"]
    
    search_fields = ["title"]

    ordering = ["title"]

    empty_value_display = '-empty-'

    actions = [make_published]
    
    #list_filter = ["created_date"]
    list_filter = ["content"]
    
    def view_created_date(self,obj):
        return obj.created_date
    
    view_created_date.empty_value_display = '???'

    class Meta:
        model = Article