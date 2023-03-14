from django.shortcuts import render

# Create your views here.
def jinja_printing(request):
    d={'name':'sekhar','age':21}
    return render(request,'jinja_printing.html',context=d)
