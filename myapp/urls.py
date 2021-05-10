from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('brand',views.brand,name='brand'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('seller_add_product',views.seller_add_product,name='seller_add_product'),
    path('seller_index',views.seller_index,name='seller_index'),
    path('seller_view_product',views.seller_view_product,name='seller_view_product'),
    path('seller_edit_product/<int:pk>/',views.seller_edit_product,name='seller_edit_product'),
    path('seller_product_details/<int:pk>/',views.seller_product_details,name='seller_product_details'),
    path('seller_delete_product/<int:pk>/',views.seller_delete_product,name='seller_delete_product'),
    path('user_product_detail/<int:pk>/',views.user_product_detail,name='user_product_detail'),
    path('add_to_wishlist/<int:pk>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('mywishlist',views.mywishlist,name='mywishlist'),
    path('remove_from_wishlist/<int:pk>/',views.remove_from_wishlist,name='remove_from_wishlist'),
    path('add_to_cart/<int:pk>/',views.add_to_cart,name='add_to_cart'),
    path('mycart',views.mycart,name='mycart'),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart,name='remove_from_cart'),
    path('change_password',views.change_password,name='change_password'),
    path('change_qty',views.change_qty,name='change_qty'),
    path('pay',views.initiate_payment,name='pay'),
    path('callback/',views.callback, name='callback'),
    path('myorder',views.myorder,name='myorder'),
    path('user_order_detils/<int:pk>/',views.user_order_detils,name='user_order_detils'),
    path('user_edit_profile',views.user_edit_profile,name='user_edit_profile'),
    path('user_product_search',views.user_product_search,name='user_product_search'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('enter_email',views.enter_email,name='enter_email'),
    path('forgot_verify_otp',views.forgot_verify_otp,name='forgot_verify_otp'),
    path('new_password',views.new_password,name='new_password'),
    path('seller_change_password',views.seller_change_password,name='seller_change_password'),
    path('seller_enter_email',views.seller_enter_email,name='seller_enter_email'),
    path('seller_forgot_verify_otp',views.seller_forgot_verify_otp,name='seller_forgot_verify_otp'),
    path('seller_new_password',views.seller_new_password,name='seller_new_password'),
    path('ajax/login_validate_email/',views.login_validate_email,name='login_validate_email'),
    path('ajax/signup_validate_email/',views.signup_validate_email,name='signup_validate_email'),
    path('seller_edit_profile',views.seller_edit_profile,name='seller_edit_profile'),
    
]        