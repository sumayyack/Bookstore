from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from book.models import Book,Orders
from django.views.generic import TemplateView,ListView
from book.models import Cart
from django.contrib import messages
from django.utils.decorators import method_decorator
from book.decorators import signin_required
from django.db.models import Sum
# Create your views here.
@method_decorator(signin_required,name="dispatch")
class CustomerHome(TemplateView):
    def get(self,request,*args,**kwargs):
        books = Book.objects.all()
        context = {"books": books}
        return render(request, "home.html", context)


#def customer_home(request):
 #   books=Book.objects.all()
  #  context={"books":books}
   # return render(request,"home.html",context)

class SignUpView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = forms.UserRegistrationForm()
        context = {"form": form}
        return render(request,"userregistration.html",context)
    def post(self,request):
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print("user hasbeen registered")
            return redirect("signin")



#def sign_up(request):
#    form=forms.UserRegistrationForm()
#    context={"form":form}
#    if request.method=="POST":
#        form=forms.UserRegistrationForm(request.POST)
#        if form.is_valid():
#            form.save()
#            print("user hasbeen registered")
#            return redirect("signin")
#    return render(request,"userregistration.html",context)

class SignInView(TemplateView):
    def get(self, request, *args, **kwargs):
        form=forms.LoginForm
        return render(request, "login.html", {"form": form})
    def post(self,request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("customerhome")


#def sign_in(request):
#    form=forms.LoginForm()
#    if request.method=="POST":
#        form=forms.LoginForm(request.POST)
#        if form.is_valid():
#            username=form.cleaned_data["username"]
#            password=form.cleaned_data["password"]
#            user=authenticate(request,username=username,password=password)
#            if user:
#                login(request,user)
#                return redirect("customerhome")

#    return render(request,"login.html",{"form":form})

@signin_required
def sign_out(request):
    logout(request)
    return redirect("signin")

@method_decorator(signin_required,name="dispatch")
class AddToCart(TemplateView):
    model=Cart


    def get(self, request,*args,**kwargs):
        id=kwargs["id"]
        book=Book.objects.get(id=id)
        cart=Cart.objects.create(item=book,user=request.user)
        cart.save()
        print("item added to cart")
        return redirect("customerhome")

@method_decorator(signin_required,name="dispatch")
class ViewMyCart(TemplateView):
    model=Cart
    template_name = "mycart.html"
    def get(self, request, *args, **kwargs):
        context={}

        items=Cart.objects.filter(user=request.user,status="incart")
        context["items"] = items
        total=Cart.objects.filter(user=request.user,status="incart").aggregate(Sum("item__price"))
        context["total"]=total['item__price__sum']

        return render(request,self.template_name,context)

@method_decorator(signin_required,name="dispatch")
class RemoveItemFromCart(TemplateView):
    model=Cart

    def get(self, request, *args, **kwargs):
        id=kwargs["id"]
        cart=self.model.objects.get(id=id)
        cart.status="cancelled"
        cart.save()
        messages.success(request,"Item has been removed from Cart")
        return redirect("customerhome")

@method_decorator(signin_required,name="dispatch")
class OrderCreate(TemplateView):
    model=Orders
    form_class=forms.OrderForm
    template_name = "ordercreate.html"
    context={}
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        cart_id=kwargs["id"]
        cart_item=Cart.objects.get(id=cart_id)
        form=self.form_class(request.POST)
        if form.is_valid():
            address=form.cleaned_data["address"]
            user=request.user.username
            item=cart_item.item
            order=self.model.objects.create(
                item=item,
                user=user,
                addres=address,
            )
            order.save()
            cart_item.status="orderplaced"
            cart_item.save()
            messages.success(request,"orderplaced")
            return redirect("customerhome")



class ViewMyOrder(ListView):
    model=Orders
    template_name = "myorder.html"
    context_object_name = "orders"


    def get_queryset(self):
        queryset=super().get_queryset()

        queryset=self.model.objects.filter(user=self.request.user)

        return queryset