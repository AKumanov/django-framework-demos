from django.contrib import admin
from .models import Todo, Category


# Register your models here.
# admin.site.register(T-odo)
# admin.site.register(Category)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'urgency')
    list_filter = ('urgency', 'category')
    search_fields = ('title',)
    search_help_text = 'Search by Todo Title '


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

