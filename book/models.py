from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=20)
    copies=models.PositiveIntegerField(default=1)
    image=models.ImageField(upload_to="images",null=True)


    def __str__(self):
        return self.book_name

class Cart(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(("incart","incart"),
             ("cancelled","cancelled"),
             ("orderplaced","orderplaced"))
    status=models.CharField(max_length=120,choices=options,default="incart")

class Orders(models.Model):
    item=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=120)
    addres=models.CharField(max_length=120)
    date_order=models.DateField(auto_now_add=True)
    options=(("orderplaced","orderplaced"),
             ("dispatch","dispatch"),
             ("intransit","intransit"),
             ("delivered","delivered"),
             ("order_cancelled","order_cancelled"))
    status=models.CharField(max_length=120,choices=options,default="orderplaced")
    expected_delivery_date=models.DateField(null=True,blank=True)


#ORM QUERIES
#book=Book(book_name="randamoozham",author="MT",price=89,copies=90)
#books=Book.objects.all()
#books
#price<300
#books=Book.objects.filter(price__lt=300)
#pric100-300
#books=Book.objects.filter(price__gt=100,price__lt=300)
#booname=alchemist
#books=Book.objects.filter(book_name="alchemist")
#Case insensitive matching
#books=Book.objects.filter(book_name__iexact="Alchemist")
#fetching a particular object
#book=Book.objects.get(book_name="test")
#book.delete()
#fetching book id
#books=book.objects.all().values('id','book_name')
#books

