from django.contrib import admin
from .models import Category,Course
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    list_display_links = ('name',)
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name','price','available','created','updated','creater','language']
    list_editable = ['price','available']
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Course,CourseAdmin)