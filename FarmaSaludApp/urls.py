from django.conf.urls import url
from FarmaSaludApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^categoria/$',views.categoriaApi),
    url(r'^categoria/([0-9]+)$',views.categoriaApi),

    url(r'^producto/$',views.productoApi),
    url(r'^producto/([0-9]+)$',views.productoApi),
    
    url(r'^guardarImagen/$',views.guardarImagen),

    url(r'^user/$',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)