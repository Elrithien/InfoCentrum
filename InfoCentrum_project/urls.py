"""InfoCentrum_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from InfoCentrum_app.views import PurposeView, main, MaterialPersonsView, MaterialView, MaterialBrandView, CountryView, \
    AddGuestView, MaterialPersonAddView, search_category, PurposeAddView, continent, statistic, MaterialAddView, \
    modify_purpose

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name="main"),
    url(r'^purposes/$', PurposeView.as_view(), name='purposes' ),
    url(r'^add_purpose/', PurposeAddView.as_view(), name='add_purpose'),
    url(r'^modify_purpose/(?P<id>[0-9]+)/$', modify_purpose, name='modify_purpose'),
    url(r'^material_persons/$', MaterialPersonsView.as_view(), name='material_persons'),
    url(r'^material_person/(?P<id>(\d)+)/$', MaterialPersonAddView.as_view(), name='material_person'),
    url(r'^materials/$', MaterialView.as_view(), name='materials'),
    url(r'^brands/$', MaterialBrandView.as_view(), name='brands'),
    url(r'^countries/$', CountryView.as_view(), name='countries'),
    url(r'^add_guest/$', AddGuestView.as_view(), name='add_guest'),
    url(r'^material_person_add/$', MaterialPersonAddView.as_view(), name='material_person_add'),
    url(r'^search_purpose/(?P<text>\w+)/$', search_category, name='search_category'),
    url(r'^continent/$', continent, name='continent'),
    url(r'^statistic/$', statistic, name='statistic'),
    url(r'^material_add/$', MaterialAddView.as_view(), name='material_add'),

]
