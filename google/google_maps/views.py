from django.shortcuts import render

# Create your views here.



from django.http import HttpResponse





def index(request):
    return HttpResponse("hello all we are at google maps")
def maps(request):
    return render(request, 'maps/maps.html')