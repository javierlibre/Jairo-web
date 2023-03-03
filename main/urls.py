from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('galeria', views.galeria, name='galeria'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('blog', views.blog, name='blog'),
    path('contacto', views.contacto, name='contacto'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)