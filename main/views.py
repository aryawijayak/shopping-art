from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Lukisan Arya Ganteng ',
        'amount': 2000000,
        'description': 'Lukisan langka hanya ada satu satunya di dunia'
    }

    return render(request, "main.html", context)
