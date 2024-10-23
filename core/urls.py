from django.urls import path
from .views import *

urlpatterns = [
    path('load-districts/', load_districts, name="load_districts"),
    path('load-sub-districts/', load_sub_districts, name="load_sub_districts"),
    path('about-us/', about, name="about_us"),
    path('faqs/', faqs, name="faqs"),
    path('terms-condition/', terms_condition, name="terms_condition"),
    path('privacy-policy/', privacy_policy, name="privacy_policy"),
]