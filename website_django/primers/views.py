from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from primers.models import Primer

# Create your views here.
def IndexView(generic.ListView):
  # show the latest 25 primers
  template_name = 'primers/index.html'
  context_object_name = 'latest_primer_list'

  def get_queryset(self):
    """Return the last 25 designed primers."""
    return Primer.objects.order_by('-id')[:25]

def DetailView(generic.DetailView):
  model = Primer
  template_name = 'primers/detail.html'

def edit(request, primer_id):
  p = get_object_or_404(Primer, pk=primer_id)
  
  return HttpResponseRedirect(reverse('primers:detail', args=(p.id,)))
