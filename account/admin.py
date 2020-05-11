from django.contrib import admin
from .models import Jobs

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('date', 'invoiceno', 'externalno', 'ticket', 'location', 'sordescription', 'rate', 'qty', 'gst', 'total')
    list_display_links = ('externalno', 'ticket', 'location',)
    search_fields = ('externalno', 'ticket', 'location', 'sordescription', 'rate', 'invoiceno' )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Jobs, AccountAdmin)