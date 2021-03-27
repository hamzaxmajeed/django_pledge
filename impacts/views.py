from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import Bills, Veg

# function based views
def home(request):
    """
    displays all pledges data fields

    :param request: HttpRequest object which contains the data 
    :return: renders the template home.html
    """
    bills = Bills.objects.all()
    vegs = Veg.objects.all()
    
    return render(request, 'impacts/home.html', {'bills': bills, 'vegs': vegs})


def bills(request):
    """
    displays the bills data fields

    :param request: HttpRequest object which contains the data 
    :return: renders the template home.html
    """
    if request.GET:
        if request.method == 'GET':
            energy = request.GET.get('energy')
            people = request.GET.get('people')
            people = int(float(people))
            heat = request.GET.get('heat')
            name = request.GET.get('name')
            message = request.GET.get('message')

            if energy == 'bog standard':
                a = 0.5
            else:
                a = 0

            if heat == 'electricity':
                b = 3
            else:
                b = 5

            impact = int(49 * a * b * people)

            try:
                bill = Bills.objects.create(name=name, energy_supplier=energy,
                    num_of_people=people, heating_source=heat, message=message, impact=impact)
                bill.save()
                
            except ObjectDoesNotExist:
                pass

            return render(request, 'impacts/bills.html', {'impact' : impact})

    else:
        return render(request, 'impacts/bills.html')


def veg(request):
    """
    displays the veg out data fields

    :param request: HttpRequest object which contains the data 
    :return: renders the template veg.html
    """
    if request.GET:
        if request.method == 'GET':
            current = request.GET.get('current')
            current = int(float(current))
            veggie = request.GET.get('veggie')
            name = request.GET.get('name')
            message = request.GET.get('message')

            if veggie == '0-5':
                a = 2.5
            else:
                a = 3

            co_impact = 0.884 * a * 8.7
            water_impact = 0.75 * current
            waste_impact = 0.2 * current * a

            try:
                veg_out = Veg.objects.create(name=name, current_meals=current,
                    veggie_meals=veggie, co_impact=co_impact, water_impact=water_impact,
                        waste_impact=waste_impact, message=message)
                veg_out.save()

            except ObjectDoesNotExist:
                pass

            return render(request, 'impacts/veg.html', {'co_impact': co_impact, 'waste_impact': waste_impact, 'water_impact': water_impact})

    return render(request, 'impacts/veg.html' )
