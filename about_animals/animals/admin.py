from email._header_value_parser import Comment

from django.contrib import admin

from animals.models import *


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('kind', 'birthday', 'image')
    readonly_fields = ('birthday', )
    list_filter = ('birthday', )
    search_fields = ('kind', 'birthday')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    fields = ('author', 'text', 'date', 'img')
    list_display = ('author', 'date', 'img')
    readonly_fields = ('date',)
    list_filter = ('date',)
    search_fields = ('author', 'text')




