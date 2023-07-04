from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# task 1
# def home(request):
#     return render(request, "Home.html")
#
#
# def about(request):
#     return HttpResponse("<h1><b>ABOUT</b></h1>")
#
#
# def contact(request):
#     return render(request, "Contact.html")
#
#
# def detail(request):
#     return HttpRespopnse("<h1><b>DETAILS</b></h1>")
#
#
# def thanks(request):
#     return render(request, "Thanks.html")


# task 2

def first(request):
    return render(request, "1st page.html")


def ops(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    add = (x + y)
    sub = (x - y)
    mul = (x * y)
    div = (x / y)
    return render(request, "2nd page.html",
                  {'result1': add, 'result2': sub, 'result3': mul, 'result4': div, 'n1': x, 'n2': y})
