from django.contrib import admin
from .models import Contact,Jamoa,Article,Comment,Port
# Register your models here.

admin.site.register((Port,Contact))



# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     list_display=["title","create_data","is_active"]
#     list_filter = ["is_active"]

@admin.register(Jamoa)
class JamoaAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]

admin.site.register(Comment)