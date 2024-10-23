from django.shortcuts import render, redirect, get_object_or_404
import datetime
from django.core.paginator import Paginator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import *
from core.models import *
from Store.models import *
from PaymentApp.models import *
from UserAccount.models import *


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'dashboard/index.html')


## ============= User =============
@login_required
def user_list(request):
    get_status = request.GET.get('get_status', 'All')
    if get_status == 'is_customer':
        obj_list = CustomUser.objects.filter(is_active=True ,is_customer=True)
    elif get_status == 'is_staff':
        obj_list = CustomUser.objects.filter(is_active=True ,is_staff=True, is_superuser=False)
    elif get_status == 'is_superuser':
        obj_list = CustomUser.objects.filter(is_active=True ,is_superuser=True)
    else:
        obj_list = CustomUser.objects.filter(is_active=True)
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    context = {
        'query': query, 
        'get_status':get_status,
    }
    return render(request, 'dashboard/user/list.html', context)

@login_required
def user_add(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def user_edit(request, id):
    obj = get_object_or_404(CustomUser, id=id)
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = CustomUserForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form': form, "from_user":True})


@login_required
def user_change_password(request, id):
    obj = CustomUser.objects.get(id=id)
    if request.method == "POST":
        form = PasswordChangeForm(user=obj, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('user_list')
        else:
            return redirect('user_list')
    form = PasswordChangeForm(user=obj)
    return render(request, 'dashboard/user/change-password.html', {'form': form})

@login_required
def user_delete(request, id):
    CustomUser.objects.get(id=id).delete()
    return redirect("user_list")


## ============================= Location data Start ===========================
## ============= Division =============
@login_required
def division_list(request):
    obj_list = Division.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/location-data/division/list.html', {'query': query})

@login_required
def division_add(request):
    if request.method == 'POST':
        form = DivisionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('division_list')
    else:
        form = DivisionForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def division_edit(request, id):
    obj = Division.objects.get(id=id)
    if request.method == 'POST':
        form = DivisionForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('division_list')
    else:
        form = DivisionForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def division_delete(request, id):
    Division.objects.get(id=id).delete()
    return redirect('division_list')



## ============= District ==============
@login_required
def district_list(request):
    obj_list = District.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/location-data/district/list.html', {'query': query})

@login_required
def district_add(request):
    if request.method == 'POST':
        form = DistrictForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('district_list')
    else:
        form = DistrictForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def district_edit(request, id):
    obj = District.objects.get(id=id)
    if request.method == 'POST':
        form = DistrictForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('district_list')
    else:
        form = DistrictForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})


@login_required
def district_delete(request, id):
    District.objects.get(id=id).delete()
    return redirect('district_list')




## ============= Sub District ==========
@login_required
def sub_district_list(request):
    obj_list = SubDistrict.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/location-data/sub_district/list.html', {'query': query})

@login_required
def sub_district_add(request):
    if request.method == 'POST':
        form = SubDistrictForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sub_district_list')
    else:
        form = SubDistrictForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def sub_district_edit(request, id):
    obj = SubDistrict.objects.get(id=id)
    if request.method == 'POST':
        form = SubDistrictForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('sub_district_list')
    else:
        form = SubDistrictForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def sub_district_delete(request, id):
    SubDistrict.objects.get(id=id).delete()
    return redirect('sub_district_list')

## ============================= Location data End =============================



## ============================= Web data Start =============================
## ============= Website information ==============

@login_required
def website_info_list(request):
    obj_list = WebsiteInfo.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/web-data/web-info/list.html', {'query': query})

@login_required
def website_info_add(request):
    if request.method == 'POST':
        form = WebsiteInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('website_info_list')
    else:
        form = WebsiteInfoForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def website_info_edit(request, id):
    obj = WebsiteInfo.objects.get(id=id)
    if request.method == 'POST':
        form = WebsiteInfoForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('website_info_list')
    else:
        form = WebsiteInfoForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def website_info_delete(request, id):
    WebsiteInfo.objects.get(id=id).delete()
    return redirect('website_info_list')



## ============= Terms & Condition ==============

@login_required
def terms_conditions_list(request):
    obj_list = TermsCondition.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/web-data/terms/list.html', {'query': query})

@login_required
def terms_conditions_add(request):
    if request.method == 'POST':
        form = TermsConditionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('terms_conditions_list')
    else:
        form = TermsConditionForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def terms_conditions_edit(request, id):
    obj = TermsCondition.objects.get(id=id)
    if request.method == 'POST':
        form = TermsConditionForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('terms_conditions_list')
    else:
        form = TermsConditionForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def terms_conditions_delete(request, id):
    TermsCondition.objects.get(id=id).delete()
    return redirect('terms_conditions_list')


## ============= Faqs ==============

@login_required
def faqs_list(request):
    obj_list = faq.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/web-data/faq/list.html', {'query': query})

@login_required
def faqs_add(request):
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('faqs_list')
    else:
        form = FaqForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def faqs_edit(request, id):
    obj = faq.objects.get(id=id)
    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('faqs_list')
    else:
        form = FaqForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def faqs_delete(request, id):
    faq.objects.get(id=id).delete()
    return redirect('faqs_list')

## ============= Privacy & Policy ==============

@login_required
def privacy_policys_list(request):
    obj_list = PrivacyPolicy.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/web-data/privacy-policy/list.html', {'query': query})

@login_required
def privacy_policys_add(request):
    if request.method == 'POST':
        form = PrivacyPolicyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('privacy_policys_list')
    else:
        form = PrivacyPolicyForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def privacy_policys_edit(request, id):
    obj = PrivacyPolicy.objects.get(id=id)
    if request.method == 'POST':
        form = PrivacyPolicyForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('privacy_policys_list')
    else:
        form = PrivacyPolicyForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def privacy_policys_delete(request, id):
    PrivacyPolicy.objects.get(id=id).delete()
    return redirect('privacy_policys_list')



## ============================= Web data End =============================


## ============= Privacy & Policy ==============
@login_required
def about_us_list(request):
    obj_list = AboutUs.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/web-data/about-us/list.html', {'query': query})

@login_required
def about_us_add(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_us_list')
    else:
        form = AboutUsForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def about_us_edit(request, id):
    obj = AboutUs.objects.get(id=id)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('about_us_list')
    else:
        form = AboutUsForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def about_us_delete(request, id):
    AboutUs.objects.get(id=id).delete()
    return redirect('about_us_list')




## ===================== Support Section ==================
@login_required
def support_section_list(request):
    obj_list = SupportSection.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/web-data/support/list.html', {'query': query})

@login_required
def support_section_add(request):
    if request.method == 'POST':
        form = SupportSectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('support_section_list')
    else:
        form = SupportSectionForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def support_section_edit(request, id):
    obj = SupportSection.objects.get(id=id)
    if request.method == 'POST':
        form = SupportSectionForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('support_section_list')
    else:
        form = SupportSectionForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def support_section_delete(request, id):
    SupportSection.objects.get(id=id).delete()
    return redirect('support_section_list')



## ========================= Shipping Address start ============================
@login_required
def shipping_address_list(request):
    obj_list = ShippingAddress.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/shipping-data/shipping-address/list.html', {'query': query})

@login_required
def shipping_address_add(request):
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shipping_address_list')
    else:
        form = ShippingAddressForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def shipping_address_edit(request, id):
    obj = ShippingAddress.objects.get(id=id)
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('shipping_address_list')
    else:
        form = ShippingAddressForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def shipping_address_delete(request, id):
    ShippingAddress.objects.get(id=id).delete()
    return redirect('shipping_address_list')

##==============================Shipping Adress End ===============================

## ============================ Banner start =================================
##  ================ Banner ====================
@login_required
def banner_list(request):
    obj_list = Banner.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/banner/main-banner/list.html', {'query': query})

@login_required
def banner_add(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = BannerForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def banner_edit(request, id):
    obj = Banner.objects.get(id=id)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('banner_list')
    else:
        form = BannerForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def banner_delete(request, id):
    Banner.objects.get(id=id).delete()
    return redirect('banner_list')

## ================== Offer Banner =========================
@login_required
def offer_banner_list(request):
    obj_list = OfferBanner.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/banner/offer-banner/list.html', {'query': query})

@login_required
def offer_banner_add(request):
    if request.method == 'POST':
        form = OfferBannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('offer_banner_list')
    else:
        form = OfferBannerForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def offer_banner_edit(request, id):
    obj = OfferBanner.objects.get(id=id)
    if request.method == 'POST':
        form = OfferBannerForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('offer_banner_list')
    else:
        form = OfferBannerForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def offer_banner_delete(request, id):
    OfferBanner.objects.get(id=id).delete()
    return redirect('offer_banner_list')
##  ========================== Offer Banner end ===================================

## ============================ Blog start =================================
@login_required
def blog_list(request):
    obj_list = blog.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/blog-data/blogs/list.html', {'query': query})

@login_required
def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def blog_edit(request, id):
    obj = blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('blog_list')
    else:
        form = BlogForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def blog_delete(request, id):
    blog.objects.get(id=id).delete()
    return redirect('blog_list')


## =============== Blog Comments =======================
@login_required
def blog_comment_list(request):
    obj_list = BlogComment.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/blog-data/blog-comments/list.html', {'query': query})

@login_required
def blog_comment_add(request):
    if request.method == 'POST':
        form = BlogCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_comment_list')
    else:
        form = BlogCommentForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def blog_comment_edit(request, id):
    obj = BlogComment.objects.get(id=id)
    if request.method == 'POST':
        form = BlogCommentForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('blog_comment_list')
    else:
        form = BlogCommentForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def blog_comment_delete(request, id):
    BlogComment.objects.get(id=id).delete()
    return redirect('blog_comment_list')
##  ========================== Blog end ===================================

## ========================== Order Data Start =======================================
## ======================= Orders ==========================
@login_required
def order_list(request):
    get_status = request.GET.get('get_status', 'All')
    if get_status!= 'All':
        obj_list = Order.objects.filter(status=get_status)
    else:
        obj_list = Order.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)

    total_orders = Order.objects.all().count()
    pending_orders = Order.objects.filter(status='Pending').count()
    complete_orders = Order.objects.filter(status='Complete').count()
    cancel_orders = Order.objects.filter(status='Cancel').count()
    process_ontheway = Order.objects.filter(status__in=['Process', 'On the Way']).count()
    context = {
        'query': query, 
        'get_status':get_status,
        "total_orders":total_orders,
        "pending_orders":pending_orders,
        "complete_orders":complete_orders,
        "cancel_orders":cancel_orders,
        "process_ontheway":process_ontheway,
    }
    return render(request, 'dashboard/order/list.html', context)

@login_required
def order_details(request, id):
    query = get_object_or_404(Order, id=id)
    shipping_address = ShippingAddress.objects.filter(order__id=id, order__user=request.user).last()
    order_items = query.items.all() 

    context = {
        'query': query,
        'shipping_address': shipping_address,
        'order_items': order_items,
    }
    return render(request, 'dashboard/order/overview.html', context)


@login_required
def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def order_edit(request, id):
    obj = get_object_or_404(Order, id=id)

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            order = form.save(commit=False)
            status = form.cleaned_data['status']
            if status == 'Complete':
                order.complete_date = datetime.datetime.now()
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def order_cancel(request):
    order_id = request.GET.get('order_id')
    obj = Order.objects.get(id=order_id)
    obj.status = 'Cancel'
    obj.save()
    return redirect("order_details", id=order_id)

@login_required
def order_delete(request, id):
    Order.objects.get(id=id).delete()
    return redirect("order_list")


## ========================== Product Data Start =======================================
## ======================= Products ==========================

# @login_required
# def pending_product(request):
#     obj_list = Product.objects.filter(is_show=False)
#     paginator = Paginator(obj_list, 10)
#     page_number = request.GET.get("page")
#     query = paginator.get_page(page_number)
#     return render(request, 'dashboard/product-data/product/list.html', {'query': query})

@login_required
def product_list(request):
    is_show = request.GET.get('is_show')
    if is_show is not None:
        obj_list = Product.objects.filter(is_show=(is_show == 'True'))
    else:
        obj_list = Product.objects.all()
        
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/product-data/product/list.html', {'query': query, 'is_show': is_show})


@login_required
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            if form.cleaned_data['is_show']:
                return redirect('accepted_product')
            else:
                return redirect('pending_product')
    else:
        form = ProductForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def product_edit(request, id):
    obj = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            if form.cleaned_data['is_show']:
                return redirect('product_list')
            else:
                return redirect('product_list')
            # return redirect('accepted_product') if form.cleaned_data['is_show'] else redirect('pending_product')
    else:
        form = ProductForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def product_delete(request, id):
    Product.objects.get(id=id).delete()
    red_page = request.META.get('HTTP_REFERER', 'pending_product')
    return redirect(red_page)


## ================= Product Category ==========================
@login_required
def product_category_list(request):
    obj_list = ProductCategory.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/product-data/product-category/list.html', {'query': query})

@login_required
def product_category_add(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_category_list')
    else:
        form = ProductCategoryForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def product_category_edit(request, id):
    obj = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('product_category_list')
    else:
        form = ProductCategoryForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def product_category_delete(request, id):
    ProductCategory.objects.get(id=id).delete()
    return redirect('product_category_list')



## ============= Size ============================
@login_required
def size_list(request):
    obj_list = Size.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/product-data/size/list.html', {'query': query})

@login_required
def size_add(request):
    if request.method == 'POST':
        form = SizeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('size_list')
    else:
        form = SizeForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def size_edit(request, id):
    obj = Size.objects.get(id=id)
    if request.method == 'POST':
        form = SizeForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('size_list')
    else:
        form = SizeForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def size_delete(request, id):
    Size.objects.get(id=id).delete()
    return redirect('size_list')


## ===================== Product ==================
@login_required
def color_list(request):
    obj_list = Color.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/product-data/color/list.html', {'query': query})

@login_required
def color_add(request):
    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('color_list')
    else:
        form = ColorForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def color_edit(request, id):
    obj = Color.objects.get(id=id)
    if request.method == 'POST':
        form = ColorForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('color_list')
    else:
        form = ColorForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def color_delete(request, id):
    Color.objects.get(id=id).delete()
    return redirect('color_list')
## ========================== Product Data end =======================================



## ============== Coupon =========================

@login_required
def coupon_list(request):
    obj_list = Coupon.objects.all()
    paginator = Paginator(obj_list, 10)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)
    return render(request, 'dashboard/product-data/coupon/list.html', {'query': query})

@login_required
def coupon_add(request):
    if request.method == 'POST':
        form = CouponForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('coupon_list')
    else:
        form = CouponForm()
    return render(request, 'dashboard/base-full-form.html', {'form': form})

@login_required
def coupon_edit(request, id):
    obj = Coupon.objects.get(id=id)
    if request.method == 'POST':
        form = CouponForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('coupon_list')
    else:
        form = CouponForm(instance=obj)
    return render(request, 'dashboard/base-full-form.html', {'form':form})

@login_required
def coupon_delete(request, id):
    Coupon.objects.get(id=id).delete()
    return redirect('coupon_list')





