from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id","first_name"]

@admin.register(Baby)
class BabyAdmin(admin.ModelAdmin):
    list_display = ["id","first_name","last_name"]
