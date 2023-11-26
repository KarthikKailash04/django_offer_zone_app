from django.shortcuts import render
from store.models import Product
from django.utils import timezone


def home(request):
    product=Product.objects.all()
    context={ "product":product ,}
    print(timezone.now())
    return render(request,'home.html',context)