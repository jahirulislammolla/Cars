from django.shortcuts import render,redirect
from .models import Cars,Manufactuers
# Create your views here.
def home(request):
    return render(request,'home.html',{})
def add_multi_cars(request):
    context={}
    context['cars']=[]
    if request.method == 'POST' and request.POST.get('submit') == 'submit_car_number':
        for i in range(1,int(request.POST.get('car_number'))+1):
            context['cars']+=[i]
        return render(request, 'add_multi_cars.html', context)
        if request.method == 'POST' and request.POST.get('submit') == 'submit_car':
            pass
    return render(request,'add_multi_cars.html',context)
def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        year = request.POST.get('year')
        manufactuer = request.POST.get('manufactuer')
        image = request.FILES.get('image')
        obj=Cars(name=name,year=year,manufactuer=manufactuer,image=image)
        obj.save()
        return redirect('/')
    return render(request,'add_car.html',{})


def add_manufactuer(request):
    if request.method == "POST":
        name=request.POST.get('name')
        country=request.POST.get('country')
        logo=request.FILES.get('logo')
        obj=Manufactuers(name=name,country=country,logo=logo)
        obj.save()
        return redirect('/')
    return render(request,'add_manufactuer.html',{})