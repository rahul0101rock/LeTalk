from django.contrib import admin

# Register your models here.
from .models import user_search,friends_list,request_list

class friend_list_admin(admin.ModelAdmin):
    class Meta:
        model = friends_list

admin.site.register(friends_list, friend_list_admin)

class request_list_admin(admin.ModelAdmin):
    class Meta:
        model = request_list

admin.site.register(request_list, request_list_admin)