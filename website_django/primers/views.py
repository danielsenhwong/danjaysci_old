from django.shortcuts import render

# Create your views here.
def index(request):
  latest_primer_list = Primer.objects.order_by('-id')[:5]
  output = ', '.join([p for p in latest_primer_list])
  return HttpResponse(output)

def detail(request, primer_id):
  return HttpResponse("Primer detail of %s" % primer_id)


