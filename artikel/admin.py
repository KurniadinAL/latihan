from django.contrib import admin

# Register your models here.
from .models import Artikel, Category

class ArtikelAdmin(admin.ModelAdmin):
	readonly_fields=[
		'slug',
		'updated',
		'published',
	]

admin.site.register(Artikel, ArtikelAdmin)

class CategoriAdmin(admin.ModelAdmin):
	readonly_fields=[
		'updated',
		'published',
	]

admin.site.register(Category, CategoriAdmin)