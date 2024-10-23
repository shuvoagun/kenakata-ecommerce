from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import *
from .forms import *


# Create your views here.
def home(request):
    products = Product.objects.filter(is_show=True)
    categories = ProductCategory.objects.all()
    banners = Banner.objects.all()
    offer_banners = OfferBanner.objects.all().order_by('-id')[:4]
    supports = SupportSection.objects.all().last()
    blogs = blog.objects.all()

    context = {
        'products':products,
        'categories':categories,
        'banners':banners,
        'offer_banners':offer_banners,
        'supports':supports,
        'blogs':blogs,
    }
    return render(request, 'store/index.html',context)



def product_page(request):
    products = Product.objects.filter(is_show=True)
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)

    categories = ProductCategory.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    context = {
        'query':query,
        'categories':categories,
        'sizes':sizes,
        'colors':colors,
    }
    return render(request, 'store/product-page.html',context)



def product_category_page(request, id):
    category = ProductCategory.objects.get(id=id)
    size_id = request.GET.get('size_id')
    color_id = request.GET.get('color_id')
    sort_by = request.GET.get('sort-by', 'id')
    color = None
    size = None
    if color_id:
        color = Color.objects.get(id=color_id)
    if size_id:
        size = Size.objects.get(id=size_id)

    if size:
        products = Product.objects.filter(is_show=True, category=category, size__name__icontains=size).order_by(sort_by)
    if color:
        products = Product.objects.filter(is_show=True, category=category, color__name__icontains=color).order_by(sort_by)
    if size and color:
        products = Product.objects.filter(is_show=True, category=category, size__name__icontains= size, color__name__icontains=color).order_by(sort_by)
    else:
        products = Product.objects.filter(is_show=True, category=category).order_by(sort_by)
    paginator = Paginator(products, 1)
    page_number = request.GET.get("page")
    query = paginator.get_page(page_number)

    categories = ProductCategory.objects.all()
    sizes = Size.objects.all()
    colors = Color.objects.all()
    context = {
        'category':category,
        'size':size,
        'color':color,
        'query':query,
        'categories':categories,
        'sizes':sizes,
        'colors':colors,
    }
    return render(request, 'store/product-page.html',context)



def product_details(request, id):
    product = Product.objects.get(id=id)
    products = Product.objects.filter(id=product.id)
    new_products = Product.objects.filter(is_show=True)

    context = {
        'product':product,
        'products':products,
        'new_products':new_products
    }
    return render(request, 'store/product-accordion-full-width.html', context)


@login_required
def add_to_cart(request):
    index = request.POST.get('index')
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    product = Product.objects.get(id=product_id)
    order_item, created = OrderItem.objects.get_or_create(
        product=product,
        user=request.user,
        ordered=False,
    )
    if created:
        order_item.quantity = quantity
        order_item.save()
        messages.success(request, "Added to cart")

        order, created = Order.objects.get_or_create(
            user=request.user,
            ordered = False
        )
        if created:
            order.items.add(order_item)
            order.status = 'Pending'
            order.save()
        else:
            order.items.add(order_item)
            order.save()
    else:
        order_item.quantity += quantity
        order_item.save()
        messages.success(request, "Increment Quantity")
    if index:
        return redirect('home')
    else:
        return redirect('product_details', id=product_id)

@login_required
def remove_to_cart(request, id):
    OrderItem.objects.get(id=id).delete()
    messages.success(request, "Removed Successfully")
    return redirect('carts')

@login_required
def carts(request):
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    order = Order.objects.filter(user=request.user, ordered=False).last()
    products = Product.objects.filter(is_show=True)
    return render(request, 'store/cart.html',{'order':order,'order_items':order_items,'products':products})

@login_required
def cart_quantity_increment(request):
    order_item_id = request.POST.get('order_item_id')
    order_item = OrderItem.objects.get(id=order_item_id)
    if order_item.quantity <= order_item.product.stock:
        order_item.quantity += 1
        order_item.save()
        messages.success(request, 'Order quantity Increase')
    else:
        messages.error(request, 'Out of stock')
    return redirect('carts')

@login_required
def cart_quantity_decrement(request):
    order_item_id = request.POST.get('order_item_id')
    order_item = OrderItem.objects.get(id=order_item_id)
    if order_item.quantity > 1:
        order_item.quantity -= 1
        order_item.save()
        messages.success(request, 'Order quantity Decrease')
    else:
        messages.error(request, 'Quantity should be more than 1')
    return redirect('carts')


@login_required
def wishlist(request):
    wish_list = Wishlist.objects.filter(user=request.user)
    products = Product.objects.filter(is_show=True)
    context = {
        'wish_list':wish_list,
        'products':products
        }
    return render(request, 'store/wishlist.html', context)




@login_required
def add_to_wishlist(request):
    product_id = request.GET.get('product_id')
    home = request.GET.get('home', None)
    product = Product.objects.get(id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(product=product, user=request.user)
    if created:
        messages.success(request, 'Product added to wishlist')
    else:
        messages.warning(request, 'Product already in wishlist')
    if home:
        return redirect('home')
    else:
        return redirect('product_details', id=product.id)


@login_required
def remove_to_wishlist(request, id):
    Wishlist.objects.get(id=id).delete()
    messages.success(request, "Removed Successfully")
    return redirect('wishlist')

def blog_full_width(request):
    blogs = blog.objects.all()
    
    context = {
        'blogs':blogs
    }
    return render(request, 'store/blog-full-width.html', context)



def blog_details(request, id):
    blogs = blog.objects.get(id=id)
    comments = BlogComment.objects.filter(blog=blogs)
    comments_count = BlogComment.objects.filter(blog=blogs).count()
    user_form = BlogCommentForm() 
    if request.method == 'POST':
        user_form = BlogCommentForm(request.POST)
        if user_form.is_valid():
            obj = user_form.save(commit=False)
            obj.blog = blogs
            obj.save()
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Somthing went Wrong!')

    context = {
        'blogs': blogs,
        'user_form': user_form,
        'comments': comments,
        'comments_count': comments_count,
    }
    return render(request, 'store/blog-detail-full-width.html', context)



def contact(request):
    user_form = ContactUsForm() 

    if request.method == 'POST':
        user_form = ContactUsForm(request.POST)
        if user_form.is_valid():
            user_form.save() 
            messages.success(request, 'Your message has been sent successfully!')
        else:
            messages.error(request, 'Somthing went Wrong!')

    context = {
        'user_form': user_form,
    }
    return render(request, 'store/contact-us.html', context)













def compare(request):
    return render(request, 'store/compare.html')











def track_order(request):
    return render(request, 'store/track-order.html')



