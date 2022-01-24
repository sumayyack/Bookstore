from django.shortcuts import redirect

def signin_required(fun):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fun(request,*args,**kwargs)
    return wrapper


def admin_permission_required(fun):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_superuser:
            return redirect("signin")
        else:
            return fun(request,*args,**kwargs)

    return wrapper