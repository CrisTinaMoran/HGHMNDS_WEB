from django.contrib import admin
from .models import Item
from .models import User

admin.site.register(Item)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'role') 
    list_filter = ('role',)             
    search_fields = ('username',)       

# Register your models here.
