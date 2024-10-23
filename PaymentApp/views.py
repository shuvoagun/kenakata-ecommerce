from django.shortcuts import render, redirect
from Store.models import Order, OrderItem, Product, Coupon
from django.contrib.auth.decorators import login_required
from .forms import ShippingAddressForm
from django.contrib import messages
from django.utils import timezone
from .models import ShippingAddress

# Create your views here.

@login_required
def checkout(request):
    shipping_request = request.GET.get('shipping_data', '')
    if shipping_request:
        shipping_data = ShippingAddress.objects.filter(order__user=request.user).last()
    else:
        shipping_data = ''
    order = Order.objects.filter(user=request.user, ordered=False).last()
    order_items = OrderItem.objects.filter(user=request.user, ordered=False)
    products = Product.objects.filter(is_show=True)
    
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            o = form.save()
            o.order = order
            o.save()

            type = form.cleaned_data['type']
            payment_type = request.POST['payment_type']
            for item in order_items:
                item.ordered = True
                item.save()

                product = Product.objects.get(id=item.product.id)
                product.stock -= item.quantity
                product.save()

            order.shipping_charge(type)
            order.amount = order.total_amount()
            order.due_amount = order.get_due_amount()
            order.payment_type = payment_type
            order.status = "Pending"
            order.ordered = True
            order.save()

            messages.success(request, "Checkout completed successfully")
            return redirect('home')
        else:
            print(form.errors)
    
    context = {
        'order':order,
        'order_items':order_items,
        'products':products,
        'shipping_data':shipping_data,
        }
    return render(request, 'paymentApp/checkout.html', context)

@login_required
def apply_coupon(request):
    now = timezone.now()
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')
        order = Order.objects.filter(user=request.user, ordered=False).last()
        coupon = Coupon.objects.get(code=coupon_code)
        if coupon:
            if coupon.start_date <= now and coupon.end_date >= now and coupon.quntity > coupon.used:
                order.coupon = coupon
                order.save()
                coupon.used += 1
                coupon.save()
                messages.success(request, "Coupon applied successfully")
                return redirect('checkout')
            else:
                messages.error(request, "Coupon is expired or not available")
                return redirect('checkout')
        else:
            messages.error(request, "Coupon Doesn't Exist")
            return redirect('checkout')