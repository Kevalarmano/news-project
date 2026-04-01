from django.http import HttpResponse

def home(request):
    """Return a simple homepage response."""
    return HttpResponse("News Project Running")
