import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import FormView, CreateView
from django.template.response import TemplateResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from itertools import zip_longest


from django.db.models import Avg, Min

from InfoCentrum_app.forms import MaterialPersonAddForm, AddGuestForm, PurposeAddForm, MaterialAddForm
from .models import Guest, Purpose, MaterialGuest, Material, MaterialPerson, MaterialBrand, Country
# from .forms import


def main(request):
    return render(request, "main.html")



### =-=-=-=-=-=-= Purpose =-=-=-=-=-=-=
class PurposeView(View):

    def get(self, request):
        purposes = Purpose.objects.all().order_by('id')
        return render(request, "PurposeView.html", {'purposes': purposes})


class PurposeAddView(View):

    def get(self, request):
        form = PurposeAddForm()
        return render(request, "PurposeAddView.html", {'form': form})

    def post(self, request):
        form = PurposeAddForm(request.POST)
        if form.is_valid():
            p = Purpose.objects.create(
                purpose = form.cleaned_data['purpose'])


            return redirect(reverse('add_purpose', args=[p.id]))

        return render(request, "PurposeAddView.html", {'form': form})




def search_category(request, text):
    purposes = Purpose.objects.filter(purpose__icontains=text)
    return HttpResponse(json.dumps([{"id":purpose.pk, "purpose":purpose.purpose} for purpose in purposes]))


def modify_purpose(request, id):
    purpose = Purpose.objects.get(id=id)
    if request.method == 'GET':
        context = {
            'purpose': purpose
        }
        return render(request, "PurposeModifyView.html", context=context)
    elif request.method == 'POST':
        modified_purpose = request.POST.get('modified_purpose')
        purpose.purpose = modified_purpose
        purpose.save()
        return redirect('purposes')


### =-=-=-=-=-=-= END Purpose =-=-=-=-=-=-=


### =-=-=-=-=-=-= Material (Materials, Material Persons, Material Brands =-=-=-=-=-=-=
#Materials
class MaterialView(View):

    def get(self, request):
        materials = Material.objects.all()
        return render(request, "MaterialView.html", {'materials': materials})


class MaterialAddView(View):

    def get(self, request):
        form = MaterialAddForm()
        return render(request, "MaterialAddView.html", {'form': form})

    def post(self, request):
        form = MaterialAddForm(request.POST)
        if form.is_valid():
            m = form.cleaned_data['material']
            form.save()

            return redirect(reverse('material_add', args=[m.id]))

        return render(request, "MaterialAddView.html", {'form': form})



#Material Persons
class MaterialPersonsView(View):

    def get(self, request):
        persons = MaterialPerson.objects.all()
        return render(request, "MaterialPersonsView.html", {'persons': persons})


class MaterialPersonAddedView(View):

    def get(self, request):
        brands = MaterialBrand.objects.all()
        return render(request, "MaterialBrandView.html", {'brands': brands})


class MaterialPersonAddView(View):

    def get(self, request):
        form = MaterialPersonAddForm()
        return render(request, "MaterialPersonAddView.html", {'form': form})

    def post(self, request):
        form = MaterialPersonAddForm(request.POST)
        if form.is_valid():
            p = MaterialPerson.objects.create(
                name = form.cleaned_data['name'],
                brand = form.cleaned_data['brand'],
                phone = form.cleaned_data['phone'],
                email = form.cleaned_data['email'],

            )
            # form.save()

            return redirect(reverse('material_person', args=[p.id]))

        return render(request, "MaterialPersonAddView.html", {'form': form})

#Material Brands
class MaterialBrandView(View):

    def get(self, request):
        brands = MaterialBrand.objects.all()
        return render(request, "MaterialBrandView.html", {'brands': brands})


### =-=-=-=-=-=-= END Material (Material, Material Person, Material Brand =-=-=-=-=-=-=


### =-=-=-=-=-=-= Country =-=-=-=-=-=-=

def getCountry(countries):
    return [country.country for country in countries]

class CountryView(View):

    def get(self, request):
        countries = Country.objects.all()
        europe = getCountry(Country.objects.filter(continent="Europa"))
        asia = getCountry(Country.objects.filter(continent="Azja"))
        america_s = getCountry(Country.objects.filter(continent="Am. Południowa"))
        america_n = getCountry(Country.objects.filter(continent="Am. Północna"))
        australia = getCountry(Country.objects.filter(continent="Australia i Oceania"))
        africa = getCountry(Country.objects.filter(continent="Afryka"))
        undefined = getCountry(Country.objects.filter(continent="Nieokreślony"))


        longest = list(zip_longest(europe, asia, america_n, america_s, australia, africa, undefined, fillvalue=""))
        # for europe, asia, america_n, america_s, australia, africa, undefined in longest:
        #     print(europe, asia, america_n, america_s, australia, africa, undefined)
        #print(longest)

        return render(request, "CountryView.html", {'longest': longest,
                                                    'europe': europe})

### =-=-=-=-=-=-= END Country =-=-=-=-=-=-=


### =-=-=-=-=-=-= Guest =-=-=-=-=-=-=
class AddGuestView(View):

    def get(self, request):
        form = AddGuestForm()
        return render(request, "AddGuestView.html", {'form': form})

    def post(self, request):
        form = AddGuestForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect(reverse('add_guest'))

        return render(request, "AddGuestView.html", {'form': form})


class GuestView(View):

    def get(self, request):
        guests = Guest.objects.all()
        return render(request, "AddGuestView.html", {'guests': guests})


### =-=-=-=-=-=-= END Guest =-=-=-=-=-=-=


### =-=-=-=-=-=-= Continent =-=-=-=-=-=-=

def continent(request):
    return render(request, "ContinentView.html")

### =-=-=-=-=-=-= END Continent =-=-=-=-=-=-=


### =-=-=-=-=-=-= Statistic =-=-=-=-=-=-=

def statistic(request):
    return render(request, "StatisticView.html")

### =-=-=-=-=-=-= END Statistic =-=-=-=-=-=-=










