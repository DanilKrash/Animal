from django.contrib import admin

from animals.models import *


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('kind', 'birthday', 'image')
    readonly_fields = ('birthday', )
    list_filter = ('birthday', )
    search_fields = ('kind', 'birthday')



