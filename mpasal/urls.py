from django.contrib import admin
from django.urls import path, include
from apps.core.views import ProductListView, SearchListView, order_confirmation
from apps.store.views import productDetailView, categoryDetail
from django.conf import settings
from django.conf.urls.static import static
from apps.store.api import api_add_to_cart, api_checkout, api_remove_from_cart
from apps.cart.views import cart_detail,tests
from apps.coupons.api import api_can_use

admin.site.site_header = 'mPasal'
admin.site.site_title = 'mPasal Admin Portal'
admin.site.index_title =  'Welcome to the future'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',ProductListView.as_view(),name='frontpage'),

    path('order_confirmation/',order_confirmation, name='order_confirmation'),

    path('accounts/', include('allauth.urls')),

    path('cart/',cart_detail,name='cart_detail'),

    path('search/',SearchListView.as_view(),name='search'),

    #api cart

    path('api/can_use/',api_can_use,name='api_can_use'),

    path('api/add_to_cart/',api_add_to_cart,name='api_add_to_cart'),

    path('api/checkout/' ,api_checkout,name='api_checkout'),

    path('api/remove_from_cart/', api_remove_from_cart, name='api_remove_from_cart'),


#cat
    path('<slug:slug>/',categoryDetail,name='categories_detail'),
    
    path('<slug:category_slug>/<slug:slug>/',productDetailView,name='product_detail'),


    


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

