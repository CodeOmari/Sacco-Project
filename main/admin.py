from django.contrib import admin

from main.models import Customer, Deposits

# Register your models here.

# run manage.py file
# python manage.py --help
# python manage.py createsuperuser-admin@gmail.com, 12345678
# Run localhost:8000/admin


# customize site name
admin.site.site_header = 'Umoja Sacco Administration'

# customize title
admin.site.site_title = 'Sacco Admin'

# customize what you want to display from your models
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'dob']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['gender']
    list_per_page = 25

class DepositsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'amount', 'status', 'created_at']
    search_fields = ['amount', 'status']
    list_per_page = 25
    list_editable = ['status']


# add Models
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposits, DepositsAdmin)

# hr@645Company
