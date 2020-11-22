from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Cars,Manufactuers
from itertools import chain
# Create your views here.


#home page view......
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
                name = request.POST.get('name_'+str(i)).upper()
                year = request.POST.get('year_'+str(i))
                manufactuer = request.POST.get('manufactuer_'+str(i)).upper()
                image = request.FILES.get('image_'+str(i))
                obj = Cars(name=name, year=year, manufactuer=manufactuer, image=image)
                obj.save()
            context = Cars.objects.all()
            return render(request, 'all_cars.html', {'data': context})
    return render(request,'add_multi_cars.html',context)

#add single car data...
def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name_1').upper()
        year = request.POST.get('year_1')
        manufactuer = request.POST.get('manufactuer_1').upper()
        image = request.FILES.get('image_1')
        obj=Cars(name=name,year=year,manufactuer=manufactuer,image=image)
        obj.save()
        context = Cars.objects.all()
        return render(request, 'all_cars.html', {'data': context})
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

#show all manufactuers....
def all_manufactuers(request):
    context=Manufactuers.objects.all()
    return render(request, 'all_manufactuers.html', {'data': context})

#delete manufactuer....
def delete_manufactuer(request):
    id = request.GET.get('id', None)
    del_row=Manufactuers.objects.get(id=id)
    del_row.delete()
    return HttpResponse("Success!")  # Sending an success response

#delete car....
def delete_car(request):
    id=request.GET.get('id', None)
    del_row=Cars.objects.get(id=id)
    del_row.delete()
    return HttpResponse("Success!") #sending an sucess response

#check manufactuer existed or not......
def check_manufactuer(request):
    name= request.GET.get('name', None).upper()
    check=Manufactuers.objects.filter(name=name).count()
    print(check)
    return JsonResponse({'count':check})

def country_wise_manufactuer(request):
    cars=Cars.objects.all()
    manufactuers=Manufactuers.objects.all()
    data_manufactuer={}
    data_car={}
    for i in manufactuers:
        if i.country not in data_manufactuer:
            data_manufactuer[i.country]=[]
        data_manufactuer[i.country]+=[i.name]
        data_car[i.name] = []
    for i in cars:
        if i.manufactuer in data_car:
            data_car[i.manufactuer]+=[i]
    return render(request,'country_wise_manufactuer.html',{ "data_car":data_car, "data_manufactuer":data_manufactuer})
from django.template.defaulttags import register

@register.filter(name='get_item')
def get_item(dictionary, key):
    if dictionary.get(key) == None:
        return "a"
    return dictionary.get(key)
