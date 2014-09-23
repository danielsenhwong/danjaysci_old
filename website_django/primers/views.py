from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from primers.models import Primer

# Create your views here.
class IndexView(generic.ListView):
  # show the latest 25 primers
  template_name = 'primers/index.html'
  context_object_name = 'primer_list'

  def get_queryset(self):
    """Return a list of primers, newest first."""
    return Primer.objects.order_by('-id')

class DetailView(generic.DetailView):
  model = Primer
  template_name = 'primers/detail.html'

def edit(request, primer_id):
  p = get_object_or_404(Primer, pk=primer_id)
  
  return HttpResponseRedirect(reverse('primers:detail', args=(p.id,)))
