from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    context = {
        'name': 'Lukisan Arya Ganteng ',
        'amount': 2000000,
        'description': 'Lukisan langka hanya ada satu satunya di dunia'
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_main(request):
    products = Product.objects.all()

    context = {
        'products': products,

        'karya1': 'Online Course App', 
        'artist1': 'Arya Wijaya Kusuma', 

        'karya2': 'Private Tutor App', 
        'artist2': 'Arya keren',

        'karya3': 'Task Management App', 
        'artist3': 'Aweka Design',
        'total' : products.__len__(),
    }

    return render(request, "main.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

