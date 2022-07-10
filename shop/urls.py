from django.urls import path

from . import views

urlpatterns = [
    path('store/', views.StoreView.as_view()),
    path('store/<str:store_name>/', views.StoreProductsView.as_view()),
    path('product/<str:product_name>/', views.ProductView.as_view()),
    path('product/<str:product_name>/review/', views.ProductReviewView.as_view()),
    path('product/', views.ProductSortView.as_view()),
    path('category/', views.CategoryView.as_view()),
    path('category/<str:category_name>/', views.CategoryProductView.as_view()),
]
