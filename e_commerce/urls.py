from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', include('order.urls')),
    path('user/', include('user.urls')),
    path('', include('shop.urls')),
]
