from django.contrib import admin

# Register your models here.
from .models import User, Item

class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'pwd')
    search_fields = ('phone',)
    list_per_page = 10

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'ques', 'ans', 'author', 'add')
    search_fields = ('ques',)
    list_per_page = 10

admin.site.register(User, UserAdmin)
admin.site.register(Item, ItemAdmin)