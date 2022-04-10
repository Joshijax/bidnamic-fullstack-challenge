from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns,static
from django.urls import path



 
urlpatterns = [
     path('', views.Home, name='home'),
     path('dashboard', views.Dashboard, name='dashboard'),
     path('login', views.Login, name='login'),
     path('logout/', views.logout_request, name='logout'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)