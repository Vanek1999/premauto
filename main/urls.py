from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about-us', views.about_us, name='about_us'),
    path('shop', views.shop, name='shop'),
    path('my-account', views.my_account, name='my_account'),
    path('cart', views.cart, name='cart'),
    path('spares', views.spares, name='spares'),
    path('autochemistry', views.autochemistry, name='autochemistry'),
    path('oil', views.oil, name='oil'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
