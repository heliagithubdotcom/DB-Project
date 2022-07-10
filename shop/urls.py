from django.urls import path

from . import views

urlpatterns = [
    path('store/<str:store_name>/', views.StoreProductsView.as_view()),
    path('product/<str:product_name>/', views.ProductView.as_view()),
    path('product/<str:product_name>/review/', views.ProductReviewView.as_view()),
    path('product/', views.ProductSortView.as_view()),
]
