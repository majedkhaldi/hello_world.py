from django.shortcuts import render, redirect
from .models import Order, Product
from django.db.models import Sum

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
    quantity_from_form = int(request.POST["quantity"])
    idofproduct = int(request.POST["price"])
    price_from_form = Product.objects.get(id = idofproduct).price
    total_charge = quantity_from_form * price_from_form
    request.session['total_charge'] = float(total_charge)
    ordersproducts = Order.objects.aggregate(total =Sum("quantity_ordered"))
    ordersprices = Order.objects.aggregate(total =Sum("total_price"))
    request.session['result1'] = ordersproducts['total']
    request.session['result2'] = float(ordersprices['total'])
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price= total_charge)
    return redirect('/showcheckout')

def checkoutdispaly(request):
    return render(request, "store/checkout.html")
