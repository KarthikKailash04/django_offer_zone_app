from django.db import models
from Category.models import category
from django.urls import reverse
from django.utils import timezone
from background_task import background

class Product(models.Model):
    offer=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,null=True)
    discription = models.TextField(max_length=300,blank=True)
    #price=models.IntegerField()
    images = models.ImageField(upload_to='photos/offers')
    #stock = models.IntegerField()
    #is_available=models.BooleanField(default=True)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    offer_shop_pincode=models.CharField( max_length=6,null=True)
    starting_date=models.DateTimeField(null=True)
    ending_date=models.DateTimeField()
    number=models.CharField(max_length=12,null=True)
    alt_number=models.CharField(max_length=12,null=True,blank=True)
    offer_shop_address=models.CharField(max_length=200,null=True)
    offer_shop_name=models.CharField(max_length=100)
    offer_percent = models.CharField(max_length=200,null=True)


    def __str__(self):
        return self.offer
    def get_url(self):
       return reverse('offer_detail',args=[self.category.slug,self.slug])
    
    @background(schedule=60)  
    def delete_expired_instances():
        now = timezone.now()
        expired_instances = Product.objects.filter(ending_date__lte=now)
        expired_instances.delete()