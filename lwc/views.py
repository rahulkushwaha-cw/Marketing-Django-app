import requests
from django.shortcuts import render

def index(request):
    r = requests.get('http://httpbin.org/status/418')
    print r.text
    return HttpResponse('<pre>' + r.text + '</pre>')
    
def testhome(request):
	context = {}
	template = "donotuse.html"
	return render(request,template,context)
