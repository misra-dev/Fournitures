from django.urls import path
from backend import views

urlpatterns = [
    path('', views.login, name="login"),
    path('add_category/', views.add_category, name="add-category"),
    path('get_cat/<int:pk>/', views.get_cat, name="get-cat"),
    path('get_all_cat/', views.get_categories, name="get-all-cat"),
    path('edit_cat/', views.edit_cat, name="edit-cat"),
    path('add_prod/', views.add_product, name="add-prod"),
    path('products/', views.product_list, name="product-list"),
    path('edit_prod/<int:pk>/', views.product_update, name="edit-prod"),
]