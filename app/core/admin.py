from django.contrib import admin

from core import models


class AffiliateAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name']
    readonly_fields = ['slug']


class ArticleAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'title', 'date']
    readonly_fields = ['intro', 'slug']


class ExecutiveAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'first_name', 'last_name', 'position']
    readonly_fields = ['slug']


class MessageAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'date', 'name', 'email', 'subject']
    readonly_fields = ['date', 'email', 'message', 'name', 'phone', 'subject']


class ProjectAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'name', 'category', 'contract_completion']
    readonly_fields = ['slug']


admin.site.register(models.Affiliate, AffiliateAdmin)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Executive, ExecutiveAdmin)
admin.site.register(models.Project, ProjectAdmin)
