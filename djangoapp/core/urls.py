from django.urls import path
from . import views

urlpatterns={
	path('',include('core.urls')),
	path('admin/',admin.sites.urls)
}