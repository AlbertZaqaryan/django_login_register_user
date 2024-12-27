from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login_request, name='login'),
    path('register/',views.register_request, name='register'),
    path('logout/', views.logout_request, name='logout'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('delete_from_cart/', views.delete_from_cart, name='delete_from_cart'),
    path('user_page/', views.user_page, name='user_page'),
    path('add_book/', views.add_book, name='add_book'),
]