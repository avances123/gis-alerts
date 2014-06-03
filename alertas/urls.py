from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from alertas.clientes.views import ClienteViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter(trailing_slash=False)
router.register(r'clientes', ClienteViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alertas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
)
