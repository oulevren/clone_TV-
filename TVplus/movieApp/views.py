from django.shortcuts import render,redirect

# Create your views here.


def index(request):

        # if request.user.is_authenticated:
    #     return redirect('profile')

    return render(request,"index.html")



def dashboard(request):
    return render(request,"dashboard.html")