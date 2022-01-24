from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from book.forms import BookForm,OrderUpdateForm
#from book import form
from book.models import Book,Orders
from django.views.generic import CreateView,DetailView,ListView,UpdateView,DeleteView,TemplateView
from.filters import BookFilter,OrderFilter
# Create your views here.
class BookCreateView(CreateView):
    model = Book
    form_class =BookForm
    template_name = "add_book.html"
    success_url = reverse_lazy("listbook")



class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"



class BookList(ListView):
    model= Book
    template_name = "book_list.html"
    context_object_name = "books"


class BookUpdateView(UpdateView):
    model= Book
    form_class = BookForm
    template_name = "book_edit.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")


class BookRemove(DeleteView):
    model = Book
    template_name = "removebook.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")



class ViewOrders(ListView):
    model = Orders
    template_name = "customer_orders.html"
    context_object_name = "orders"
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        neworders=self.model.objects.filter(status="orderplaced")
        context["neworders"]=neworders
        context["neworder_count"]=neworders.count()


        d_orders=self.model.objects.filter(status="delivered")
        context["d_orders"]=d_orders
        context["d_order_count"]=d_orders.count()
        return context

class OrderDetailView(DetailView):
    model=Orders
    template_name = "orderdetailview.html"
    pk_url_kwarg = "id"
    context_object_name = "order"

class OrderUpdateView(UpdateView):
    model=Orders
    template_name = "orderchange.html"
    pk_url_kwarg = "id"
    form_class =OrderUpdateForm
    success_url = reverse_lazy("vieworders")


class BookSearchView(TemplateView):
    template_name = "books.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        f=BookFilter(self.request.GET,queryset=Book.objects.all())
        context["filter"]=f
        return context


class OrderSearchView(TemplateView):
    template_name = "orders.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        f=OrderFilter(self.request.GET,queryset=Orders.objects.all())
        context["filters"]=f
        return context

def add_book(request):
    if request.method=="GET":
        form=BookForm()
        context={}
        context["form"]=form
        return render(request,"add_book.html",context)
    if request.method=="POST":
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
           # b_name=form.cleaned_data["book_name"]
          #  auth=form.cleaned_data["author"]
            #price=form.cleaned_data["price"]
          #  availability=form.cleaned_data["copies"]
          #  books=Book.objects.create(book_name=b_name,author=auth,price=price,copies=availability)
           # books.save()
            print("book saved")
            return redirect("bookadd")


        else:


            return render(request,"add_book.html",{"form":form})

def list_book(request):
    books=Book.objects.all()
    context={}
    context["books"]=books
    return render(request,"book_list.html",context)


def remove_book(request,id):
    books=Book.objects.get(id=id)
    books.delete()
    return redirect("listbook")


def change_book(request,id):
    book=Book.objects.get(id=id)
    if request.method=="GET":
       # form=BookForm(initial={
         #   "book_name":book.book_name,
         #   "author":book.author,
          #  "price":book.price,
         #   "copies":book.copies,
     #   })
        form=BookForm(instance=book)
        context={}
        context["form"]=form
        return render(request,"book_edit.html",context)

    if request.method=="POST":
        form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
           # book.book_name=form.cleaned_data["book_name"]
           # book.author=form.cleaned_data["author"]
            #book.price=form.cleaned_data["price"]
          #  book.copies=form.cleaned_data["copies"]
           # book.save()
            return redirect("listbook")



def book_details(request,id):
    book=Book.objects.get(id=id)
    context={}
    context['book']=book
    return render(request,"book_detail.html",context)