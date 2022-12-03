from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':88}
    return render(request,'conditions.html',d)
    return render(request,'conditions.html',context=d)