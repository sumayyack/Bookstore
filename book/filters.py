import django_filters
from book.models import Book
from book.models import Orders

class BookFilter(django_filters.FilterSet):
    class Meta:
        model=Book
        fields=["book_name","author","price","copies"]


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model=Orders
        fields=["item","user","date_order","status","expected_delivery_date"]