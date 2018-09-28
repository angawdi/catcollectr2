from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.index, name='index'),
	url(r'^<int:cat_id>/$', views.show, name='show'),
	url(r'post_url/$', views.post_cat, name='post_cat')
]