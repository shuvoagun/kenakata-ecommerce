from django import forms
from core.models import *
from Store.models import *
from PaymentApp.models import *
from UserAccount.models import *
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.forms import ReadOnlyPasswordHashField

## ============= CustomUser ==============
class CustomUserForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    class Meta:
        model = CustomUser
        fields = "__all__"
    

## ============================= Location data Start ===========================
## ============= Division ==============
class DivisionForm(forms.ModelForm):
    class Meta:
        model = Division
        fields = "__all__"

## ============= District ==============
class DistrictForm(forms.ModelForm):
    class Meta:
        model = District
        fields = "__all__"

## ============= SubDistrict ==============
class SubDistrictForm(forms.ModelForm):
    class Meta:
        model = SubDistrict
        fields = "__all__"

## ============= Division ==============
# class TermsConditionForm(forms.ModelForm):
#     class Meta:
#         model = TermsCondition
#         fields = "__all__"


## ============= Terms Condition Form ==============
class WebsiteInfoForm(forms.ModelForm):
    address1 = forms.CharField(widget=CKEditorUploadingWidget())
    address2 = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = WebsiteInfo
        fields = '__all__'

## ============= Terms Condition Form ==============
class TermsConditionForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = TermsCondition
        fields = '__all__'
        
## ============= Faq Form ==============
class FaqForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = faq
        fields = '__all__'
        
## ============= Privacy Policy ==============
class PrivacyPolicyForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = faq
        fields = '__all__'

# class TermsConditionAdmin(admin.ModelAdmin):
#     form = TermsConditionForm

# admin.site.register(TermsCondition, TermsConditionForm)


## ============= About Us  ==============
class AboutUsForm(forms.ModelForm):
    short_description = forms.CharField(widget=CKEditorUploadingWidget())
    description1 = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = AboutUs
        fields = '__all__'
                
## =================== SupportSection ====================
class SupportSectionForm(forms.ModelForm):
    shipping = forms.CharField(widget=CKEditorUploadingWidget())
    support = forms.CharField(widget=CKEditorUploadingWidget())
    returns = forms.CharField(widget=CKEditorUploadingWidget())
    payment = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = SupportSection
        fields = '__all__'
        
## =================== Shipptin Address ====================
class ShippingAddressForm(forms.ModelForm):
    address = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        
## =================== Banner ====================
class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'
        
        
## =================== Offer Banner ====================
class OfferBannerForm(forms.ModelForm):
    class Meta:
        model = OfferBanner
        fields = '__all__'
        
        
## =================== Blog ====================
class BlogForm(forms.ModelForm):
    short_description = forms.CharField(widget=CKEditorUploadingWidget())
    details_description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = blog
        fields = '__all__'
        
## =================== Blog Comment ====================
class BlogCommentForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = BlogComment
        fields = '__all__'
        
## =================== Product ====================
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        
## =================== Product ====================
class ProductForm(forms.ModelForm):
    short_description = forms.CharField(widget=CKEditorUploadingWidget())
    detail_description = forms.CharField(widget=CKEditorUploadingWidget())
    specific_description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'
        
## =================== Product Category ====================
class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'
        
## =================== Product Size ====================
class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        
## =================== Product Color ====================
class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        
## =================== Coupon ====================
class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = '__all__'
