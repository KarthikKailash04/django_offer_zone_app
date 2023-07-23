from django.shortcuts import render
from django.http import HttpResponse

from .forms import offerform
from accounts.models import Account
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render, get_object_or_404, redirect
from Category.models import category
from .models import Product
from django.utils.text import slugify
from datetime import datetime, timedelta
import pgeocode
from geopy.distance import geodesic

from django.db.models import Q

def store(request, category_slug=None):
    geo = pgeocode.Nominatim('IN')
    user=request.user
    if(user.id != None):
        user_location = geo.query_postal_code(user.pin_code)
        user_coordinates = (user_location.latitude, user_location.longitude)
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(category, slug=category_slug)
        products = Product.objects.filter(category=categories)
        if(user.id != None):

          products = sorted( products,key=lambda offer: geodesic(user_coordinates, (geo.query_postal_code(offer.offer_shop_pincode).latitude, geo.query_postal_code(offer.offer_shop_pincode).longitude)).kilometers)
        product_count = len(products)
    else:
        products = Product.objects.all().filter()
        if(user.id != None):      
           products = sorted(products,key=lambda offer: geodesic(user_coordinates, (geo.query_postal_code(offer.offer_shop_pincode).latitude, geo.query_postal_code(offer.offer_shop_pincode).longitude)).kilometers)
        product_count =  len(products)

    context = {
        'products': products,
        'count': product_count
    }
    return render(request, 'store/store.html', context)

def offer_detail(request,category_slug,product_slug):
    single_product=Product.objects.get(category__slug=category_slug,slug=product_slug)
    context={"product":single_product}
    return render(request,'store/offer_detail.html',context)
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            global products,product_count

            products = Product.objects.filter(Q(discription__icontains=keyword) | Q(offer__icontains=keyword))
            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)
def offer_register(request):
    
    form = offerform()
    if request.method == 'POST':
        form = offerform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            slug = slugify(instance.offer)
            instance.slug = slug
            #instance.ending_date=datetime.now()+timedelta(minutes=2)
            instance.save()
            return redirect('home')
    else:
     form = offerform()
    context = {
        'form': form,
    }
    return render(request, 'offer/offer_register.html', context)