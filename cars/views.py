from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Cars,Manufactuers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


#home page view
def home(request):
    return render(request,'home.html',{})

#add multiple cars data...
def add_multi_cars(request):
    context={}
    context['cars']=[]
    context['number']=0
    if request.method == 'POST':
        if request.POST.get('submit') == 'submit_car_number':
            for i in range(1,int(request.POST.get('car_number'))+1):
                context['cars']+=[i]
            context['number']=int(request.POST.get('car_number'))
        else:
            for i in range(1, int(request.POST.get('submit')) + 1):
                name = request.POST.get('name_'+str(i))
                year = request.POST.get('year_'+str(i))
                manufactuer = request.POST.get('manufactuer_'+str(i))
                image = request.FILES.get('image_'+str(i))
                obj = Cars(name=name, year=year, manufactuer=manufactuer, image=image)
                obj.save()
    return render(request,'add_multi_cars.html',context)

#add single car data...
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

#add manufactuer company data...
def add_manufactuer(request):
    if request.method == "POST":
        name=request.POST.get('name').upper()
        country=request.POST.get('country').upper()
        logo=request.FILES.get('logo')
        obj=Manufactuers(name=name,country=country,logo=logo)
        obj.save()
    return render(request,'add_manufactuer.html',{})

#show all cars...
def all_cars(request):
    context=Cars.objects.all()
    return  render(request, 'all_cars.html', {'data':context})
def all_manufactuers(request):
    context=Manufactuers.objects.all()
    return render(request, 'all_manufactuers.html', {'data': context})

def delete_manufactuer(request):
        id = request.GET.get('id', None)
        row=Manufactuers.objects.get(id=id)
        row.delete()
        return HttpResponse("Success!")  # Sending an success response