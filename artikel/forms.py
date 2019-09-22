from django.forms import ModelForm

from .models import Artikel, Category


class ArtikelForm(ModelForm):
	class Meta:
		model = Artikel
		fields = [
			'judul',
			'isi',
			'kategori',
		]

class CategoryForm(ModelForm):
	class Meta:
		model = Category
		fields = [
			'kategori',
		]