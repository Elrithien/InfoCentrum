from .models import *

# def teachers_cp(request):
#     return {"teachers":Teacher.objects.all()}

def guest_cp(request):
    return {"guests": Guest.objects.all()}