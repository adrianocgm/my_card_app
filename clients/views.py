from django.http import HttpResponse
from django.template import loader
from .models import Client

def clients(request):
  myclients = Client.objects.all().values()
  template =loader.get_template('all_clients.html')
  context = {
      'myclients': myclients,
  }
  return HttpResponse(template.render(context, request))

def client_details(request, id):
    myclient = Client.objects.get(id=id)
    template = loader.get_template('client_details.html')
    context = {
        'myclient' : myclient
    }
    return HttpResponse(template.render(context, request))