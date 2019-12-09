from django.shortcuts import render
from .models import Product, Contact
import math

# Create your views here.
def index(request):
    categ = Product.objects.distinct().values("category")
    allprod = []
    for cat in categ:
        prod = Product.objects.filter(category = cat['category'])
        n = len(prod)
        item = math.ceil(n/4)
        allprod.append({"prods":prod, "length":n, "nav":range(0, item-1), "categ":cat['category']})
    total_prods = {"prods": allprod}
    return render(request, "shop/index.html", total_prods)

def about(request):
    return render(request, "shop/about.html")

def contact(request):
    
    msg = ""
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact( name=name, email=email, phone=phone, desc=desc )
        contact.save()
        msg = "Request submitted successfully. We will contact you soon."
    return render(request, 'shop/contact.html', {"msg": msg})

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product = Product.objects.filter(id = myid)
    return render(request, 'shop/prodView.html', {"product": product})

def checkout(request):
    return render(request, 'shop/checkout.html')