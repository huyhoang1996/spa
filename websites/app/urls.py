from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^news/$', views.new, name='new'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),

]
    