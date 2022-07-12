from django.contrib import admin
from .models import *
# Register your models here.


class FactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'happy_clients', 'number_of_projects', 'certifications',
                    'freelance', 'hours_of_support')
    list_editable = ('happy_clients', 'number_of_projects', 'certifications',
                     'freelance', 'hours_of_support')
    list_display_links = ('id',)


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level')
    list_editable = ('name', 'level')
    list_display_links = ('id',)


class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name','category')


admin.site.register(Facts, FactsAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Project, ProjectAdmin)
