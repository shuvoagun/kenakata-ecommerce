from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),

    ## ==================== Users =================
    path('user-list/', user_list, name="user_list"),
    path('user-add/', user_add, name="user_add"),
    path('user-edit/<int:id>', user_edit, name="user_edit"),
    path('user-change-password/<int:id>', user_change_password, name="user_change_password"),
    path('user-delete/<int:id>', user_delete, name="user_delete"),

    ## ==================== Divisions =================
    path('division-list/', division_list, name="division_list"),
    path('division-add/', division_add, name="division_add"),
    path('division-edit/<int:id>', division_edit, name="division_edit"),
    path('division-delete/<int:id>', division_delete, name="division_delete"),
    
    ## ==================== District =================
    path('district-list/', district_list, name="district_list"),
    path('district-add/', district_add, name="district_add"),
    path('district-edit/<int:id>', district_edit, name="district_edit"),
    path('district-delete/<int:id>', district_delete, name="district_delete"),
    
    ## ==================== SubDistrict =================
    path('sub_district-list/', sub_district_list, name="sub_district_list"),
    path('sub_district-add/', sub_district_add, name="sub_district_add"),
    path('sub_district-edit/<int:id>', sub_district_edit, name="sub_district_edit"),
    path('sub_district-delete/<int:id>', sub_district_delete, name="sub_district_delete"),
    
    ## ==================== Website Information =================
    path('website-info-list/', website_info_list, name="website_info_list"),
    path('website-info-add/', website_info_add, name="website_info_add"),
    path('website-info-edit/<int:id>', website_info_edit, name="website_info_edit"),
    path('website-info-delete/<int:id>', website_info_delete, name="website_info_delete"),
        
    ## ==================== Terms conditions =================
    path('terms-conditions-list/', terms_conditions_list, name="terms_conditions_list"),
    path('terms-conditions-add/', terms_conditions_add, name="terms_conditions_add"),
    path('terms-conditions-edit/<int:id>', terms_conditions_edit, name="terms_conditions_edit"),
    path('terms-conditions-delete/<int:id>', terms_conditions_delete, name="terms_conditions_delete"),

    ## ==================== Faqs =================
    path('faqs-list/', faqs_list, name="faqs_list"),
    path('faqs-add/', faqs_add, name="faqs_add"),
    path('faqs-edit/<int:id>', faqs_edit, name="faqs_edit"),
    path('faqs-delete/<int:id>', faqs_delete, name="faqs_delete"),
    
    ## ==================== Terms conditions =================
    path('privacy-policys-list/', privacy_policys_list, name="privacy_policys_list"),
    path('privacy-policys-add/', privacy_policys_add, name="privacy_policys_add"),
    path('privacy-policys-edit/<int:id>', privacy_policys_edit, name="privacy_policys_edit"),
    path('privacy-policys-delete/<int:id>', privacy_policys_delete, name="privacy_policys_delete"),
    
    ## ==================== About Us  =================
    path('about-us-list/', about_us_list, name="about_us_list"),
    path('about-us-add/', about_us_add, name="about_us_add"),
    path('about-us-edit/<int:id>', about_us_edit, name="about_us_edit"),
    path('about-us-delete/<int:id>', about_us_delete, name="about_us_delete"),

    ## ======================= Support Section =============================== 
    path('support-section-list/', support_section_list, name="support_section_list"),
    path('support-section-add/', support_section_add, name="support_section_add"),
    path('support-section-edit/<int:id>', support_section_edit, name="support_section_edit"),
    path('support-section-delete/<int:id>', support_section_delete, name="support_section_delete"),
    
    ## ==================== Shipping Address ===============================
    path('shipping-address-list/', shipping_address_list, name="shipping_address_list"),
    path('shipping-address-add/', shipping_address_add, name="shipping_address_add"),
    path('shipping-address-edit/<int:id>', shipping_address_edit, name="shipping_address_edit"),
    path('shipping-address-delete/<int:id>', shipping_address_delete, name="shipping_address_delete"),

    ## ======================= Banner =============================
    path('banner-list/', banner_list, name="banner_list"),
    path('banner-add/', banner_add, name="banner_add"),
    path('banner-edit/<int:id>', banner_edit, name="banner_edit"),
    path('banner-delete/<int:id>', banner_delete, name="banner_delete"),
    
    ## ====================== Offer Banner ============================  
    path('offer-banner-list/', offer_banner_list, name="offer_banner_list"),
    path('offer-banner-add/', offer_banner_add, name="offer_banner_add"),
    path('offer-banner-edit/<int:id>', offer_banner_edit, name="offer_banner_edit"),
    path('offer-banner-delete/<int:id>', offer_banner_delete, name="offer_banner_delete"),
    
    ## ======================= Blog =============================== 
    path('blog-list/', blog_list, name="blog_list"),
    path('blog-add/', blog_add, name="blog_add"),
    path('blog-edit/<int:id>', blog_edit, name="blog_edit"),
    path('blog-delete/<int:id>', blog_delete, name="blog_delete"),
    
    ## ======================= Blog Comments =============================== 
    path('blog-comment-list/', blog_comment_list, name="blog_comment_list"),
    path('blog-comment-add/', blog_comment_add, name="blog_comment_add"),
    path('blog-comment-edit/<int:id>', blog_comment_edit, name="blog_comment_edit"),
    path('blog-comment-delete/<int:id>', blog_comment_delete, name="blog_comment_delete"),
        
    ## ====================== Order =======================================
    path('order-list/', order_list, name="order_list"),
    path('order-overview/<int:id>', order_details, name="order_details"),
    path('order-add/', order_add, name="order_add"),
    path('order-edit/<int:id>', order_edit, name="order_edit"),
    path('order-cancel/', order_cancel, name="order_cancel"),
    path('order-delete/<int:id>', order_delete, name="order_delete"),

    ## ====================== Product =======================================
    # path('pending-product/', pending_product, name="pending_product"),
    path('product-list/', product_list, name="product_list"),
    path('product-add/', product_add, name="product_add"),
    path('product-edit/<int:id>', product_edit, name="product_edit"),
    path('product-delete/<int:id>', product_delete, name="product_delete"),
    
    ## ======================= Product Category =============================== 
    path('product-category-list/', product_category_list, name="product_category_list"),
    path('product-category-add/', product_category_add, name="product_category_add"),
    path('product-category-edit/<int:id>', product_category_edit, name="product_category_edit"),
    path('product-category-delete/<int:id>', product_category_delete, name="product_category_delete"),
     
    ## ======================= Size =============================== 
    path('size-list/', size_list, name="size_list"),
    path('size-add/', size_add, name="size_add"),
    path('size-edit/<int:id>', size_edit, name="size_edit"),
    path('size-delete/<int:id>', size_delete, name="size_delete"),
        
    ## ======================= Color =============================== 
    path('color-list/', color_list, name="color_list"),
    path('color-add/', color_add, name="color_add"),
    path('color-edit/<int:id>', color_edit, name="color_edit"),
    path('color-delete/<int:id>', color_delete, name="color_delete"),
    
    ## ======================= Coupun =============================== 
    path('coupon-list/', coupon_list, name="coupon_list"),
    path('coupon-add/', coupon_add, name="coupon_add"),
    path('coupon-edit/<int:id>', coupon_edit, name="coupon_edit"),
    path('coupon-delete/<int:id>', coupon_delete, name="coupon_delete"),
    
    
]