"""final_project_SDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from final_project_SDA import settings

from admin_accounts.views import AdminLoginView, AdminPasswordChangeView, SignUpView
from utils.views import FrontView, AboutView, HowToShopView, \
    ConditionsView, CompleteListView, ProductDetailView, FrontFefcoListView, OrderSummaryView, CheckoutView, \
    PaymentView, add_to_cart, remove_from_cart, reduce_quantity_item, ProductView, LayerListView, LayerCreateView, \
    LayerUpdateView, FrontLayerListView, AuthFrontView, search_product
from utils.views import boxes, BoxesListView, BoxUpdateView, BoxDeleteView, ToStockUpdateView, BoxCreateView, \
    FefcoListView, FefcoCreateView, FefcoUpdateView


app_name = 'utils'

urlpatterns = [

    path('admin/', admin.site.urls),


    path('utils/', BoxesListView.as_view(), name='utils'),
    path('accounts/', include('django.contrib.auth.urls')),

    path('utils/goods/update/<pk>', BoxUpdateView.as_view(), name='box_update'),
    path('utils/goods/delete/<pk>', BoxDeleteView.as_view(), name='box_delete'),
    path('utils/goods/stock/<pk>', ToStockUpdateView.as_view(), name='box_stock'),
    path('utils/goods/create', BoxCreateView.as_view(), name='box_create'),
    path('utils/fefco', FefcoListView.as_view(), name='fefco'),
    path('utils/fefco/create', FefcoCreateView.as_view(), name='fefco_create'),
    path('utils/fefco/update/<pk>', FefcoUpdateView.as_view(), name='fefco_update'),
    path('utils/layer', LayerListView.as_view(), name='layer'),
    path('utils/layer/create', LayerCreateView.as_view(), name='layer_create'),
    path('utils/layer/update/<pk>', LayerUpdateView.as_view(), name='layer_update'),


    path('utils/accounts/login/', AdminLoginView.as_view(), name='admin_login'),
    path('utils/accounts/logout/', LogoutView.as_view(), name='admin_logout'),
    path('utils/accounts/password-change/', AdminPasswordChangeView.as_view(), name='admin_password_change'),
    path('utils/accounts/sign-up/', SignUpView.as_view(), name='sign_up'),
    path('utils/login', AdminLoginView.as_view(), name='admin_login_main'),

    path('', FrontView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('how/', HowToShopView.as_view(), name='how_to_shop'),
    path('conditions/', ConditionsView.as_view(), name='conditions'),
    path('utils/bad-auth/', AuthFrontView.as_view(), name='bad_auth'),
    path('search/', search_product, name='search'),

    path('products/', CompleteListView.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/fefco/<str:fefco>/', FrontFefcoListView.as_view(), name='fefco_products'),
    path('products/layer/<str:layer>/', FrontLayerListView.as_view(), name='layer_products'),

    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-to-cart/<pk>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<pk>/', remove_from_cart, name='remove-from-cart'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item'),

    path('<pk>/', ProductView.as_view(), name='product'),


]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)