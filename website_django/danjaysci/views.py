from django.shortcuts import render_to_response, RequestContext

def home(request):
  return render_to_response('base.html', RequestContext(request, {}))
