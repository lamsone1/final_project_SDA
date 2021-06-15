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
from django.urls import path

from utils.views import boxes, BoxesListView, BoxUpdateView, BoxDeleteView, ToStockUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('utils/goods', boxes, name='boxes'),
    path('utils', BoxesListView.as_view(), name='utils'),
    path('movie/update/<pk>', BoxUpdateView.as_view(), name='box_update'),
    path('movie/delete/<pk>', BoxDeleteView.as_view(), name='box_delete'),
    path('movie/stock/<pk>', ToStockUpdateView.as_view(), name='box_stock'),

]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)