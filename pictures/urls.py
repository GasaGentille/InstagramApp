from django.conf.urls import url
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.image,name = 'image'),
    url('profile',views.profile, name='profile'),
]