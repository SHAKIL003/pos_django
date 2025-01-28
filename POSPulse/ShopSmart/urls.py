from django.urls import path
from . import views

urlpatterns = [
    # Brands
    path('brands/', views.brand_list, name='brand_list'),
    path('brands/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('brands/add/', views.add_brand, name='add_brand'),
    path('brands/update/<int:brand_id>/', views.update_brand, name='update_brand'),
    path('brands/delete/<int:brand_id>/', views.delete_brand, name='delete_brand'),

    # Mobiles
    path('mobiles/', views.mobile_list, name='mobile_list'),
    path('mobiles/<int:mobile_id>/', views.mobile_detail, name='mobile_detail'),
    path('mobiles/add/', views.add_mobile, name='add_mobile'),
    path('mobiles/update/<int:mobile_id>/', views.update_mobile, name='update_mobile'),
    path('mobiles/delete/<int:mobile_id>/', views.delete_mobile, name='delete_mobile'),

    # Specifications
    path('mobiles/<int:mobile_id>/specifications/add/', views.add_specification, name='add_specification'),
    path('specifications/update/<int:spec_id>/', views.update_specification, name='update_specification'),
    path('specifications/delete/<int:spec_id>/', views.delete_specification, name='delete_specification'),
]
