from django.contrib import admin
from book.models import Book,Category,Author
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Author)


@admin.register(Book)
class CustomerModelAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['title']