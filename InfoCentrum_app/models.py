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





#widget django autocomplete - do wybierania celi
# https://github.com/yourlabs/django-autocomplete-light

#do utworzenia krajów, należy zamienić w Słoniu z & na '
#(&Algieria&, &Afryka&), (&Angola&, &Afryka&), (&Benin&, &Afryka&), (&Botswana&, &Afryka&), (&Burkina Faso&, &Afryka&), (&Burundi&, &Afryka&), (&Czad&, &Afryka&), (&Demokratyczna Republika Konga&, &Afryka&), (&Dżibuti&, &Afryka&), (&Egipt&, &Afryka&), (&Erytrea&, &Afryka&), (&Etiopia&, &Afryka&), (&Gabon&, &Afryka&), (&Gambia&, &Afryka&), (&Ghana&, &Afryka&), (&Gwinea&, &Afryka&), (&Gwinea Bissau&, &Afryka&), (&Gwinea Równikowa&, &Afryka&), (&Kamerun&, &Afryka&), (&Kenia&, &Afryka&), (&Komory&, &Afryka&), (&Kongo&, &Afryka&), (&Lesotho&, &Afryka&), (&Liberia&, &Afryka&), (&Libia&, &Afryka&), (&Madagaskar&, &Afryka&), (&Malawi&, &Afryka&), (&Mali&, &Afryka&), (&Maroko&, &Afryka&), (&Mauretania&, &Afryka&), (&Mauritius&, &Afryka&), (&Mozambik&, &Afryka&), (&Namibia&, &Afryka&), (&Niger&, &Afryka&), (&Nigeria&, &Afryka&), (&Południowa Afryka&, &Afryka&), (&Republika Środkowoafrykańska&, &Afryka&), (&Republika Zielonego Przylądka&, &Afryka&), (&Rwanda&, &Afryka&), (&Senegal&, &Afryka&), (&Seszele&, &Afryka&), (&Sierra Leone&, &Afryka&), (&Somalia&, &Afryka&), (&Suazi&, &Afryka&), (&Sudan&, &Afryka&), (&Sudan Południowy&, &Afryka&), (&Tanzania&, &Afryka&), (&Togo&, &Afryka&), (&Tunezja&, &Afryka&), (&Uganda&, &Afryka&), (&Wybrzeże Kości Słoniowej&, &Afryka&), (&Wyspy Świętego Tomasza i Książęca&, &Afryka&), (&Zambia&, &Afryka&), (&Zimbabwe&, &Afryka&), (&Majotta&, &Afryka&), (&Reunion&, &Afryka&), (&Sahara Zachodnia&, &Afryka&), (&Somaliland&, &Afryka&), (&Wyspa Świętej Heleny, Wyspa Wniebowstąpienia i Tristan da Cunha&, &Afryka&), (&Argentyna&, &Am. Południowa&), (&Boliwia&, &Am. Południowa&), (&Brazylia&, &Am. Południowa&), (&Chile&, &Am. Południowa&), (&Ekwador&, &Am. Południowa&), (&Gujana&, &Am. Południowa&), (&Kolumbia&, &Am. Południowa&), (&Paragwaj&, &Am. Południowa&), (&Peru&, &Am. Południowa&), (&Surinam&, &Am. Południowa&), (&Urugwaj&, &Am. Południowa&), (&Wenezuela&, &Am. Południowa&), (&Bonaire&, &Am. Południowa&), (&Curaçao&, &Am. Południowa&), (&Falklandy&, &Am. Południowa&), (&Georgia Południowa i Sandwich Południowy&, &Am. Południowa&), (&Gujana Francuska&, &Am. Południowa&), (&Antigua i Barbuda&, &Am. Północna&), (&Bahamy&, &Am. Północna&), (&Barbados&, &Am. Północna&), (&Belize&, &Am. Północna&), (&Dominika&, &Am. Północna&), (&Dominikana&, &Am. Północna&), (&Grenada&, &Am. Północna&), (&Gwatemala&, &Am. Północna&), (&Haiti&, &Am. Północna&), (&Honduras&, &Am. Północna&), (&Jamajka&, &Am. Północna&), (&Kanada&, &Am. Północna&), (&Kostaryka&, &Am. Północna&), (&Kuba&, &Am. Północna&), (&Meksyk&, &Am. Północna&), (&Nikaragua&, &Am. Północna&), (&Panama&, &Am. Północna&), (&Saint Kitts i Nevis&, &Am. Północna&), (&Saint Lucia&, &Am. Północna&), (&Saint Vincent i Grenadyny&, &Am. Północna&), (&Salwador&, &Am. Północna&), (&USA&, &Am. Północna&), (&Trynidad i Tobago&, &Am. Północna&), (&Anguilla&, &Am. Północna&), (&Aruba&, &Am. Północna&), (&Bermudy&, &Am. Północna&), (&Brytyjskie Wyspy Dziewicze&, &Am. Północna&), (&Grenlandia&, &Am. Północna&), (&Gwadelupa&, &Am. Północna&), (&Kajmany&, &Am. Północna&), (&Martynika&, &Am. Północna&), (&Montserrat&, &Am. Północna&), (&Portoryko&, &Am. Północna&), (&Saba&, &Am. Północna&), (&Saint-Barthélemy&, &Am. Północna&), (&Saint-Martin&, &Am. Północna&), (&Saint-Pierre i Miquelon&, &Am. Północna&), (&Sint Eustatius&, &Am. Północna&), (&Sint Maarten&, &Am. Północna&), (&Turks i Caicos&, &Am. Północna&), (&Wyspy Dziewicze Stanów Zjednoczonych&, &Am. Północna&), (&Afganistan&, &Azja&), (&Arabia Saudyjska&, &Azja&), (&Armenia&, &Azja&), (&Azerbejdżan&, &Azja&), (&Bahrajn&, &Azja&), (&Bangladesz&, &Azja&), (&Bhutan&, &Azja&), (&Brunei&, &Azja&), (&Chiny&, &Azja&), (&Filipiny&, &Azja&), (&Gruzja&, &Azja&), (&Indie&, &Azja&), (&Indonezja&, &Azja&), (&Irak&, &Azja&), (&Iran&, &Azja&), (&Izrael&, &Azja&), (&Japonia&, &Azja&), (&Jemen&, &Azja&), (&Jordania&, &Azja&), (&Kambodża&, &Azja&), (&Katar&, &Azja&), (&Kazachstan&, &Azja&), (&Kirgistan&, &Azja&), (&Korea Południowa&, &Azja&), (&Korea Północna&, &Azja&), (&Kuwejt&, &Azja&), (&Laos&, &Azja&), (&Liban&, &Azja&), (&Malediwy&, &Azja&), (&Malezja&, &Azja&), (&Mjanma&, &Azja&), (&Mongolia&, &Azja&), (&Nepal&, &Azja&), (&Oman&, &Azja&), (&Pakistan&, &Azja&), (&Rosja&, &Azja&), (&Singapur&, &Azja&), (&Sri Lanka&, &Azja&), (&Syria&, &Azja&), (&Tadżykistan&, &Azja&), (&Tajlandia&, &Azja&), (&Timor Wschodni&, &Azja&), (&Turcja&, &Azja&), (&Turkmenistan&, &Azja&), (&Uzbekistan&, &Azja&), (&Wietnam&, &Azja&), (&Zjednoczone Emiraty Arabskie&, &Azja&), (&Cypr Północny&, &Azja&), (&Górski Karabach&, &Azja&), (&Osetia Południowa&, &Azja&), (&Palestyna&, &Azja&), (&Tajwan&, &Azja&), (&Australia&, &Australia i Oceania&), (&Fidżi&, &Australia i Oceania&), (&Kiribati&, &Australia i Oceania&), (&Nauru&, &Australia i Oceania&), (&Nowa Zelandia&, &Australia i Oceania&), (&Palau&, &Australia i Oceania&), (&Papua-Nowa Gwinea&, &Australia i Oceania&), (&Samoa&, &Australia i Oceania&), (&Mikronezja&, &Australia i Oceania&), (&Tonga&, &Australia i Oceania&), (&Tuvalu&, &Australia i Oceania&), (&Vanuatu&, &Australia i Oceania&), (&Wyspy Marshalla&, &Australia i Oceania&), (&Wyspy Salomona&, &Australia i Oceania&), (&Guam&, &Australia i Oceania&), (&Mariany Północne&, &Australia i Oceania&), (&Niue&, &Australia i Oceania&), (&Norfolk&, &Australia i Oceania&), (&Nowa Kaledonia&, &Australia i Oceania&), (&Pitcairn&, &Australia i Oceania&), (&Polinezja Francuska&, &Australia i Oceania&), (&Samoa Am.ńskie&, &Australia i Oceania&), (&Tokelau&, &Australia i Oceania&), (&Wallis i Futuna&, &Australia i Oceania&), (&Wyspa Bożego Narodzenia&, &Australia i Oceania&), (&Wyspy Cooka&, &Australia i Oceania&), (&Wyspy Kokosowe&, &Australia i Oceania&), (&Albania&, &Europa&), (&Andora&, &Europa&), (&Austria&, &Europa&), (&Belgia&, &Europa&), (&Białoruś&, &Europa&), (&Bośnia i Hercegowina&, &Europa&), (&Bułgaria&, &Europa&), (&Chorwacja&, &Europa&), (&Cypr&, &Europa&), (&Czarnogóra&, &Europa&), (&Czechy&, &Europa&), (&Dania&, &Europa&), (&Estonia&, &Europa&), (&Finlandia&, &Europa&), (&Francja&, &Europa&), (&Grecja&, &Europa&), (&Hiszpania&, &Europa&), (&Holandia&, &Europa&), (&Irlandia&, &Europa&), (&Islandia&, &Europa&), (&Liechtenstein&, &Europa&), (&Litwa&, &Europa&), (&Luksemburg&, &Europa&), (&Łotwa&, &Europa&), (&Macedonia&, &Europa&), (&Malta&, &Europa&), (&Mołdawia&, &Europa&), (&Monako&, &Europa&), (&Niemcy&, &Europa&), (&Norwegia&, &Europa&), (&Polska&, &Europa&), (&Portugalia&, &Europa&), (&Rosja&, &Europa&), (&Rumunia&, &Europa&), (&San Marino&, &Europa&), (&Serbia&, &Europa&), (&Słowacja&, &Europa&), (&Słowenia&, &Europa&), (&Szwajcaria&, &Europa&), (&Szwecja&, &Europa&), (&Turcja&, &Europa&), (&Ukraina&, &Europa&), (&Watykan&, &Europa&), (&Węgry&, &Europa&), (&UK&, &Europa&), (&Włochy&, &Europa&), (&Abchazja&, &Europa&), (&Gagauzja&, &Europa&), (&Gibraltar&, &Europa&), (&Guernsey&, &Europa&), (&Jersey&, &Europa&), (&Kosowo&, &Europa&), (&Naddniestrze&, &Europa&), (&Svalbard&, &Europa&), (&Wyspa Man&, &Europa&), (&Wyspy Owcze&, &Europa&)



