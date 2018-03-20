from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator

# Create your models here.

#Kraje z których pochodzą goście
class Country(models.Model):
    country = models.CharField(max_length=65)
    continent = models.CharField(max_length=20)

    def __str__(self):
        return self.country


#Firmy od których otrzymujemy materiały
class MaterialBrand(models.Model):
    name = models.CharField(max_length=500, unique=True)
    website = models.CharField(max_length=500)

    def __str__(self):
        return self.name

#Osoba, która dostarczyła materiały
class MaterialPerson(models.Model):
    name = models.CharField(max_length=500)
    brand = models.ForeignKey(MaterialBrand)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.brand


#Dostarczone materiały
class Material(models.Model):
    name = models.CharField(max_length=500, unique=True, help_text="Nazwa materiału")
    type = models.CharField(max_length=500, unique=True, help_text="Rodzaj materiału")
    person = models.ForeignKey(MaterialPerson, help_text="Osoba, która dostarczyła materiały")
    brand = models.ForeignKey(MaterialBrand, help_text="Firma z której jest osoba")
    date = models.DateField(auto_now=True, help_text="Data dostarczenia")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], help_text="Ilość dostarczonych materiałów")

    def __str__(self):
        return self.name, self.brand


#Materiały rozdane gościom
class MaterialGuest(models.Model):
    material = models.ForeignKey("Material")
    guest = models.ForeignKey("Guest")
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])

#Cele wizyty
class Purpose(models.Model):
    purpose = models.CharField(max_length=500, unique=True)

    def __str__(self):
        return self.purpose

#Goście odwiedzający Info
class Guest(models.Model):
    count = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    guests_coutntry = models.ForeignKey(Country)
    guests_purpose = models.ManyToManyField("Purpose")
    date = models.DateTimeField(auto_now=True)
    materials = models.ManyToManyField(Material, through="MaterialGuest")


