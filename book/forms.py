from django import forms
from django.forms import ModelForm
from book.models import Book,Orders


    #def clean(self):
      #  cleaned_data=super().clean()
      #  price=cleaned_data["price"]
       # copies=cleaned_data["copies"]

       # if price<0:
        #    msg="invalid price"
         #   self.add_error("price",msg)
      #  if copies<0:
      #      msg="invalid number"
       #     self.add_error("copies",msg)


class BookForm(ModelForm):
    class Meta:
        model=Book
        fields=["book_name","author","price","copies","image"]
        widgets={
            "book_name":forms.TextInput(attrs={'class':'form-control'}),
            "author":forms.TextInput(attrs={'class':'form-control'}),
            "price":forms.NumberInput(attrs={'class':'form-control'}),
            "copies":forms.NumberInput(attrs={'class':'form-control'}),

        }
        labels={
            "book_name":"BOOK_NAME"
        }
class OrderUpdateForm(ModelForm):
    class Meta:
        model=Orders
        fields=["status","expected_delivery_date"]
        widgets={"status":forms.Select(attrs={'class':'form-select'}),
                 "expected_delivery_date":forms.DateInput(attrs={'type':'date'})}