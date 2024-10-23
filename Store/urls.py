from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('product-page/', product_page, name="product_page"),
    path('product-category-page/<int:id>', product_category_page, name="product_category_page"),
    path('product-details/<int:id>', product_details, name="product_details"),

    path('add-to-cart/', add_to_cart, name="add_to_cart"),
    path('remove-to-cart/<int:id>/', remove_to_cart, name="remove_to_cart"),
    path('carts/', carts, name="carts"),
    path('cart-quantity-increment/', cart_quantity_increment, name="cart_quantity_increment"),
    path('cart-quantity-decrement/', cart_quantity_decrement, name="cart_quantity_decrement"),

    path('wishlist/', wishlist, name="wishlist"),
    path('add-to-wishlist/', add_to_wishlist, name="add_to_wishlist"),
    path('remove-to-wishlist/<int:id>/', remove_to_wishlist, name="remove_to_wishlist"),

    path('blog-full-width/', blog_full_width, name="blog_full_width"),
    path('blog-details/<int:id>', blog_details, name='blog_details'),
    path('contac-us/', contact, name="contact_us"),
 



    
    path('compare/', compare, name="compare"),
    path('track_order/', track_order, name="track_order"),
    
]