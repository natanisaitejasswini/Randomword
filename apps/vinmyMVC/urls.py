from django.conf.urls import url 
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_user$', views.create),
    url(r'^reset$', views.reset)

]