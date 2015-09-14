from django.http import HttpResponse


# Create a single view called index
# Each view takes in one argument - an HttpRequest - convention states it's called request
# Each view returns an HttpResponse - in this case a simple string.
def index(request):
    return HttpResponse("Rango says hey there world!")
