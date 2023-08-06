from django.contrib import admin
from .models import Advertisement



class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price', 'is_auction', 'created_date']
    actions = ['make_auction_as_true']
    list_filter = ['is_auction', 'created_at', 'title']

    fieldsets = (
        ('Общее', {'fields': ('title', 'description'), 'classes': ['collapse']}),
        ('финансы', {'fields': ('price', 'is_auction')})
    )

    admin.action('сделать торг уместным')
    def make_auction_as_true(self, request, queryset):
        queryset.update(is_auction=True)

    admin.action('отменить торг')
    def make_auction_as_true(self, request, queryset):
        queryset.update(is_auction=False)

admin.site.register(Advertisement, AdvertisementAdmin)
