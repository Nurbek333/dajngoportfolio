from django.contrib import admin
from .models import Contact, Trainer,Jamoa,Article
# Register your models here.

admin.site.register((Trainer,Contact))



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]

@admin.register(Jamoa)
class JamoaAdmin(admin.ModelAdmin):
    list_display=["title","create_data","is_active"]
    list_filter = ["is_active"]