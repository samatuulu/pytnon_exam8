from django.contrib import admin

from reporter.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description', 'photo']
    list_display_links = ['pk', 'name']
    search_fields = ['name', 'description']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['pk', 'author', 'product', 'feedback', 'point']
    list_filter = ['author', 'product']
    list_display_links = ['pk', 'author']
    search_fields = ['author', 'feecback']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
