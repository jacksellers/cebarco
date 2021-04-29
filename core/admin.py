from django.contrib import admin
from django.shortcuts import redirect
from markdownx.admin import MarkdownxModelAdmin
from image_cropping import ImageCroppingMixin

from core import models


class AffiliateAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name']
    readonly_fields = ['slug']


class ArticleAdmin(ImageCroppingMixin, MarkdownxModelAdmin):
    ordering = ['date']
    list_display = ['title', 'date', 'cropped']
    readonly_fields = ['intro', 'slug', 'cropped']

    def response_add(self, request, obj):
        return redirect(f'/admin/core/article/{obj.id}/change/')


class ExecutiveAdmin(ImageCroppingMixin, admin.ModelAdmin):
    ordering = ['rank']
    list_display = ['rank', 'first_name', 'last_name', 'position', 'cropped']
    readonly_fields = ['slug', 'cropped']

    def response_add(self, request, obj):
        return redirect(f'/admin/core/executive/{obj.id}/change/')


class GalleryImageAdmin(ImageCroppingMixin, admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'image', 'cropped', 'article', 'project']
    readonly_fields = ['cropped']

    def response_add(self, request, obj):
        return redirect(f'/admin/core/galleryimage/{obj.id}/change/')


class GalleryVideoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'video', 'article', 'project']


class MessageAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'date', 'name', 'email', 'subject']
    readonly_fields = ['date', 'email', 'message', 'name', 'phone', 'subject']


class ProjectAdmin(ImageCroppingMixin, MarkdownxModelAdmin):
    ordering = ['name']
    list_display = [
        'name', 'category', 'contract_completion', 'home_page',
        'projects_page', 'cropped'
    ]
    readonly_fields = ['slug', 'cropped']

    def response_add(self, request, obj):
        return redirect(f'/admin/core/project/{obj.id}/change/')


admin.site.register(models.Affiliate, AffiliateAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Executive, ExecutiveAdmin)
admin.site.register(models.GalleryImage, GalleryImageAdmin)
admin.site.register(models.GalleryVideo, GalleryVideoAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Project, ProjectAdmin)
