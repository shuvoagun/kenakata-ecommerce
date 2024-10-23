from django.db import models
from UserAccount.models import CustomUser
from phone_field import PhoneField
from django.utils import timezone
from django.conf import settings

# Create your models here.
class WebsiteInfo(models.Model):
    logo = models.ImageField(upload_to='web-logo')
    contact1 = PhoneField(blank=True, null=True, help_text='Contact phone number')
    contact2 = PhoneField(blank=True, null=True, help_text='Contact phone number')
    email1 = models.EmailField(blank=True, null=True)
    email2 = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address1 = models.TextField(blank=True, null=True)
    address2 = models.TextField(blank=True, null=True)
    locations = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'Website Info Id:{self.id}'
    


class Color(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model): # don't integrate on dashboard
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255)
    image = models.ImageField(upload_to='prodect/prodect-image')
    hover_image = models.ImageField(upload_to='prodect/prodect-image')
    img1 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img2 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img3 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img4 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    img5 = models.ImageField(upload_to='prodect/prodect-extra-image', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    short_description = models.TextField()
    detail_description = models.TextField()
    specific_description = models.TextField(blank=True, null=True)
    color = models.ManyToManyField(Color)
    size = models.ManyToManyField(Size)
    stock = models.IntegerField(default=0)
    is_show = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def discount_percentage(self):
        if self.discount_price and self.price:
            discount_amount = self.price - self.discount_price
            discount_percentage = (discount_amount / self.price) * 100
            return discount_percentage
        else:
            return 0



class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount_percentage = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    quntity = models.IntegerField(default=0)
    used = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class OrderItem(models.Model): # don't integrate on dashboard
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.quantity} of {self.product.title}'

    def total(self):
        if self.product.discount_price:
            total = self.product.discount_price * self.quantity
        else:
            total = self.product.price * self.quantity
        return total


class Order(models.Model): # don't integrate on dashboard
    STATUS = (
        ("Pending","Pending"),
        ("Process","Process"),
        ("On the Way","On the Way"),
        ("Complete","Complete"),
        ("Cancel","Cancel"),
    )
    PAYMENT_TYPE = (
        ("Cash On Delivery","Cash On Delivery"),
        ("Bkash","Bkash"),
        ("Nagad","Nagad"),
        ("Rocket","Rocket"),
        ("Upay","Upay"),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem, related_name='orders')
    amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    paid_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    due_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    payment_type = models.CharField(max_length=30, choices=PAYMENT_TYPE, blank=True, null=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS)
    ordered = models.BooleanField(default=False)
    complete_date = models.DateTimeField(blank=True, null=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Order #{self.id}'

    def sub_total(self):
        sub_total = 0
        for i in self.items.all():
            sub_total += i.total()
        return sub_total 

    def shipping_charge(self, value="Inside Dhaka"):
        if value=="Inside Dhaka":
            total = 80
        else:
            total = 160
        return total

    def coupon_total(self):
        if self.coupon:
            return self.coupon.discount_percentage * self.sub_total() / 100
        else:
            return 0

    def total_amount(self):
        total = (self.sub_total() + self.shipping_charge()) - self.coupon_total()
        return total
    
    def get_due_amount(self):
        return self.amount - self.paid_amount
        


class Categorys(models.Model):
    name = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='category/category-icon-image', blank=True, null=True)
    total_items = models.BigIntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title


class OfferBanner(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title

class SupportSection(models.Model):
    shipping = models.CharField(max_length=255)
    support = models.CharField(max_length=255)
    returns = models.CharField(max_length=255)
    payment = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.shipping
    
    
class blog(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    details_description = models.TextField(blank=True, null=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to='Blog-image')
    img1 = models.ImageField(upload_to='Blog-image')
    img2 = models.ImageField(upload_to='Blog-image')
    
    def __str__(self):
        return self.title
    

class BlogComment(models.Model):
    blog = models.ForeignKey(blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    


class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    massage = models.TextField(max_length=255)
    date = models.DateField(auto_created=True, auto_now_add=True)
    
    def __str__(self):
        return self.full_name
    
    
