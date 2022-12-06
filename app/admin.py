from django.contrib import admin
from .models import MyUser

# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'phone_number']
    search_fields = ['cc_holder_name', ]
    list_per_page = 30


admin.site.register(MyUser, MyUserAdmin)
