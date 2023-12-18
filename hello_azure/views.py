from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {'name': name }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')

class HelloView(APIView):
    def get(self, request):
        name = request.GET.get('name', 'World')
        return Response({"name": name})