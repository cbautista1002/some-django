from django.http import HttpResponse

def index(request):
    return HttpResponse('<h2>Hello</h2>')
