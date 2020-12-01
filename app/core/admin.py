from django.contrib import admin

from core import models


class ArticleAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'title', 'date']
    readonly_fields = ['intro']


class MessageAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'date', 'name', 'email', 'subject']
    readonly_fields = ['date', 'email', 'message', 'name', 'phone', 'subject']


class PersonAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'first_name', 'last_name', 'position']


class ProjectAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'title', 'category', 'contract_completion']


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Message, MessageAdmin)
admin.site.register(models.Person, PersonAdmin)
admin.site.register(models.Project, ProjectAdmin)
