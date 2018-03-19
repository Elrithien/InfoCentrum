from django import forms
from django.core.validators import validate_email, URLValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Purpose, Guest, MaterialBrand, MaterialPerson, Material, MaterialGuest, Country


class MaterialPersonAddForm(ModelForm):
    class Meta:
        model = MaterialPerson
        fields = '__all__'
        labels = {
            'name': 'Imię i nazwisko',
            'brand': 'Firma',
            'phone': 'Telefon',
            'email': 'Email'
        }




class AddGuestForm(ModelForm):
    class Meta:
        model = Guest
        # fields = '__all__'
        exclude = ['guests_purpose']
        labels = {
            'count': 'Liczba',
            'guests_coutntry': 'Kraj',
            'materials': 'Materiały',
        }


class PurposeAddForm(forms.Form):

    purpose = forms.CharField(label='', max_length=100, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['purpose'].widget.attrs.update({'placeholder': 'Dodaj cel'})



class MaterialAddForm(ModelForm):
    # name = forms.CharField(label='Nazwa', max_length=500, unique=True, help_text="Nazwa materiału")
    # type = forms.CharField(label='Typ', max_length=500, unique=True, help_text="Rodzaj materiału")
    # person = forms.ForeignKey(label='Przyniesione przez', MaterialPerson, help_text="Osoba, która dostarczyła materiały")
    # brand = forms.ForeignKey(label='Firma', MaterialBrand, help_text="Firma z której jest osoba")
    # date = forms.DateField(label='Data', auto_now=True, help_text="Data dostarczenia")
    # quantity = forms.PositiveIntegerField(label='Ilość', validators=[MinValueValidator(1)],
    #                                        help_text="Ilość dostarczonych materiałów")
    class Meta:
        model = Material
        fields = '__all__'
        labels = {
            'name': 'Nazwa',
            'type': 'Typ',
            'person': 'Przyniosione przez',
            'brand': 'Firma',
            'date': 'Data dostarczenia',
            'quantity': 'Ilość',
        }
