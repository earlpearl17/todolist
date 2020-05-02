from django.urls import path

from .views import index
#from . import views

urlpatterns = [
    #path(route, view, **kwargs, name)
	path('index', index)
    #path('', views.index, name='index')
]
