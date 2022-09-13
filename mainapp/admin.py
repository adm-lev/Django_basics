from django.contrib import admin
from mainapp import models as mainapp_models


@admin.register(mainapp_models.News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'preambule', 'body']


@admin.register(mainapp_models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_course_name', 'num', 'title', 'deleted']
    ordering = ['-course__name', 'num']
    list_per_page = 2
    list_filter = ['course', 'deleted', 'created']
    actions = ['mark_delete']

    def get_course_name(self, obj):
        return obj.course.name

# @admin.register(mainapp_models.Lesson)
# class LessonAdmin(admin.ModelAdmin):
#     pass
