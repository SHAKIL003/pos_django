from django.shortcuts import render, get_object_or_404, redirect
from .models import Brand, Mobile, Specification
from django.http import HttpResponse
# from django.http import JsonResponse


# Brand Views
def brand_list(request):
    brands = Brand.objects.all()
    return render(request, 'brands/brand_list.html', {'brands': brands})

# This is for testing On POSTMAN
# def brand_list(request):
#     brands = Brand.objects.all().values('id', 'name', 'logo')
#     return JsonResponse(list(brands), safe=False)

def brand_detail(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    return render(request, 'brands/brand_detail.html', {'brand': brand})

def add_brand(request):
    if request.method == 'POST':
        name = request.POST['name']
        logo = request.FILES.get('logo')
        Brand.objects.create(name=name, logo=logo)
        return redirect('brand_list')
    return render(request, 'brands/add_brand.html')

def update_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        brand.name = request.POST['name']
        if request.FILES.get('logo'):
            brand.logo = request.FILES.get('logo')
        brand.save()
        return redirect('brand_list')
    return render(request, 'brands/update_brand.html', {'brand': brand})

def delete_brand(request, brand_id):
    brand = get_object_or_404(Brand, id=brand_id)
    if request.method == 'POST':
        brand.delete()
        return redirect('brand_list')
    return render(request, 'brands/delete_brand.html', {'brand': brand})


# Mobile Views
def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'mobiles/mobile_list.html', {'mobiles': mobiles})

def mobile_detail(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)
    return render(request, 'mobiles/mobile_detail.html', {'mobile': mobile})

def add_mobile(request):
    brands = Brand.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        brand_id = request.POST['brand']
        image = request.FILES.get('image')
        brand = get_object_or_404(Brand, id=brand_id)
        Mobile.objects.create(name=name, price=price, brand=brand, image=image)
        return redirect('mobile_list')
    return render(request, 'mobiles/add_mobile.html', {'brands': brands})

def update_mobile(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)
    brands = Brand.objects.all()
    if request.method == 'POST':
        mobile.name = request.POST['name']
        mobile.price = request.POST['price']
        mobile.brand_id = request.POST['brand']
        if request.FILES.get('image'):
            mobile.image = request.FILES.get('image')
        mobile.save()
        return redirect('mobile_list')
    return render(request, 'mobiles/update_mobile.html', {'mobile': mobile, 'brands': brands})

def delete_mobile(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)
    if request.method == 'POST':
        mobile.delete()
        return redirect('mobile_list')
    return render(request, 'mobiles/delete_mobile.html', {'mobile': mobile})


# Specification Views
def add_specification(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id)
    if request.method == 'POST':
        Specification.objects.create(
            mobile=mobile,
            processor=request.POST['processor'],
            ram=request.POST['ram'],
            storage=request.POST['storage'],
            battery=request.POST['battery'],
            screen_size=request.POST['screen_size'],
            camera=request.POST['camera'],
            os=request.POST['os']
        )
        return redirect('mobile_detail', mobile_id=mobile.id)
    return render(request, 'specifications/add_specification.html', {'mobile': mobile})

def update_specification(request, spec_id):
    specification = get_object_or_404(Specification, id=spec_id)
    if request.method == 'POST':
        specification.processor = request.POST['processor']
        specification.ram = request.POST['ram']
        specification.storage = request.POST['storage']
        specification.battery = request.POST['battery']
        specification.screen_size = request.POST['screen_size']
        specification.camera = request.POST['camera']
        specification.os = request.POST['os']
        specification.save()
        return redirect('mobile_detail', mobile_id=specification.mobile.id)
    return render(request, 'specifications/update_specification.html', {'specification': specification})

def delete_specification(request, spec_id):
    specification = get_object_or_404(Specification, id=spec_id)
    mobile_id = specification.mobile.id
    if request.method == 'POST':
        specification.delete()
        return redirect('mobile_detail', mobile_id=mobile_id)
    return render(request, 'specifications/delete_specification.html', {'specification': specification})
