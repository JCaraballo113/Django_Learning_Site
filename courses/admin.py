from django.contrib import admin

from .models import Course, Step

# Register your models here.


class StepInline(admin.TabularInline):
    model = Step


class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Course, CourseAdmin)
admin.site.register(Step)
