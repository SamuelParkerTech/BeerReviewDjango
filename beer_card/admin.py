from django.contrib import admin
from .models import Beer, Review
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Beer)
class BeerAdmin(SummernoteModelAdmin):
    list_display = ('beer_name', 'slug', 'status')
    search_fields = ['beer_name', 'content',]
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('beer_name',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Review)


