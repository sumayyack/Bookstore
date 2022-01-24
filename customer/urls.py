from django.urls import path
from customer import views
#external template

urlpatterns=[
    path('home',views.CustomerHome.as_view(),name='customerhome'),
    path('accounts/users/add',views.SignUpView.as_view(),name="signup"),
    path('accounts/users/login',views.SignInView.as_view(),name="signin"),
    path('accounts/users/logout',views.sign_out,name="signout"),
    path('addtocart/<int:id>',views.AddToCart.as_view(),name="addtocart"),
    path('mycart/',views.ViewMyCart.as_view(),name="viewmycart"),
    path('carts/item/remove/<int:id>',views.RemoveItemFromCart.as_view(),name="removeitem"),
    path('books/buynow/<int:id>',views.OrderCreate.as_view(),name="createorder"),
    path('myorder/',views.ViewMyOrder.as_view(),name="viewmyorder")
]