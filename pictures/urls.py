from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    url('^$',views.image,name = 'image'),
    url(r'^profile',views.profile, name='profile'),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^add/profile$', views.add_profile, name='add_profile'),
    url(r'^edit/profile$', views.update_profile, name='edit_profile'),
    url(r'^comment/(\d+)',views.comment, name='comment'),
    url(r'^like/(\d+)',views.likes,name= 'likes'),
    url(r'^search/', views.search_results, name='search_results')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)