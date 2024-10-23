from Store.models import WebsiteInfo, Order, OrderItem, Wishlist, ProductCategory

def dynamic_data(request):
    con_web_info = WebsiteInfo.objects.last()
    con_category_10_1 = ProductCategory.objects.all()[:10]
    con_category_10_2 = ProductCategory.objects.all()[10:20]
    con_category_10_3 = ProductCategory.objects.all()[20:30]
    con_category_10_4 = ProductCategory.objects.all()[30:40]

    if request.user.is_authenticated:
        con_order_items_count = OrderItem.objects.filter(user=request.user, ordered=False).count()
        con_wish_count = Wishlist.objects.filter(user=request.user).count()
        con_order_items = OrderItem.objects.filter(user=request.user, ordered=False)
        con_order = Order.objects.filter(user=request.user, ordered=False).last()
    else:
        con_order_items_count = 0
        con_wish_count = 0
        con_order_items = ''
        con_order = ''

    return {
        'con_web_info':con_web_info,
        'con_category_10_1':con_category_10_1,
        'con_category_10_2':con_category_10_2,
        'con_category_10_3':con_category_10_3,
        'con_category_10_4':con_category_10_4,
        'con_order_items_count':con_order_items_count,
        'con_wish_count':con_wish_count,
        
        'con_order':con_order,
        'con_order_items':con_order_items,
    }