from django.urls import path
from book import views

urlpatterns=[
    path("list/",views.BookList.as_view(),name="listbook"),
    path("add",views.BookCreateView.as_view(),name="bookadd"),
    path("remove/<int:id>",views.BookRemove.as_view(),name="removebook"),
    path("change/<int:id>",views.BookUpdateView.as_view(),name="changebook"),
    path("view/<int:id>",views.BookDetailView.as_view(),name="bookdetails"),
    path("orders/list",views.ViewOrders.as_view(),name="vieworders"),
    path("orders/detail/<int:id>",views.OrderDetailView.as_view(),name="orderdetails"),
    path("orders/change/<int:id>",views.OrderUpdateView.as_view(),name="orderchange"),
    path("find",views.BookSearchView.as_view(),name="findbook"),
    path("orders/find",views.OrderSearchView.as_view(),name="findorder")
]