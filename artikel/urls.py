from django.conf.urls import url


from .views import (
	ArtikelListView, 
	ArtikelDetailView,
	ArtikelKategoriListView,
	ArtikelCreateView,
	ArtikelUpdateView,
	ArtikelDeleteView,
	DaftarKategoriView,
	CategoryCreateView,
# 	ArtikelManageView,
)

urlpatterns = [
	url(r'^artikel/update/(?P<pk>\d+)$', ArtikelUpdateView.as_view(), name='update'),
	url(r'^artikel/delete/(?P<pk>\d+)$', ArtikelDeleteView.as_view(), name='delete'),
	url(r'^tambah/$', ArtikelCreateView.as_view(), name='create'),
	url(r'^tambahkategori/$', CategoryCreateView.as_view(), name='tambahkategori'),
	url(r'^daftarKategori/', DaftarKategoriView.as_view(), name='kategori'),
	url(r'^kategori/(?P<kategori>[\w]+)/(?P<page>\d+)$', ArtikelKategoriListView.as_view(), name='category'),
	url(r'^detail/(?P<slug>[\w-]+)$', ArtikelDetailView.as_view(), name='detail'),
	url(r'^(?P<page>\d+)$', ArtikelListView.as_view(), name='list'),
	url(r'^$', ArtikelListView.as_view(), name='index'),
	# 	url(r'^manage/$', ArtikelManageView.as_view(), name='manage'),
]