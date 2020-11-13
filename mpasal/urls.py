from django.contrib import admin
from django.urls import path, include
from apps.core.views import ProductListView
from apps.store.views import productDetailView
from django.conf import settings
from django.conf.urls.static import static
from apps.store.api import api_add_to_cart


urlpatterns = [
    path('admin/', admin.site.urls),

    #path('',frontpage,name='frontpage'),

    path('',ProductListView.as_view(),name='frontpage'),
    
    path('accounts/', include('allauth.urls')),

    #api cart

    path('api/add_to_cart/',api_add_to_cart,name='api_add_to_cart'),

    #path('test/',testy,name='test')

    path('<slug:category_slug>/<slug:slug>/',productDetailView,name='product-detail'),

    


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

