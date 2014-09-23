from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from plasmids.models import Plasmid, dnaPrep, SelectionAntibiotic

# Create your views here.
class plasmidIndex(generic.ListView):
  template_name = 'plasmids/index.html'
  context_object_name = 'plasmid_list'

  def get_queryset(self):
    """Return a list of plasmids, sorted by number."""
    return Plasmid.objects.order_by('number')

class plasmidDetail(generic.DetailView):
  model = Plasmid
  tempalte_name = 'plasmids/detail.html'

def plasmidEdit(request, plasmid_id):
  l = get_object_or_404(Plasmid, pk=plasmid_id)

  return HttpResponseDirect(reverse('plasmids:detail', args=(l.id,)))


class prepIndex(generic.ListView):
  template_name = 'preps/index.html'
  context_object_name = 'prep_list'

  def get_queryset(self):
    """Return a list of preps, most recent first."""
    return dnaPrep.objects.order_by('-prep_date')

class prepDetail(generic.DetailView):
  model = dnaPrep
  tempalte_name = 'preps/detail.html'

def prepEdit(request, dnaPrep_id):
  l = get_object_or_404(dnaPrep, pk=dnaPrep_id)

  return HttpResponseDirect(reverse('preps:detail', args=(l.id,)))

class antibioticIndex(generic.ListView):
  template_name = 'antibiotics/index.html'
  context_object_name = 'antibiotic_list'

  def get_queryset(self):
    """Return a list of antibiotics, sorted alphabetically."""
    return SelectionAntibiotic.objects.order_by('+name')

class antibioticDetail(generic.DetailView):
  model = SelectionAntibiotic
  tempalte_name = 'antibiotics/detail.html'

def antibioticEdit(request, SelectionAntibiotic_id):
  l = get_object_or_404(SelectionAntibiotic, pk=SelectionAntibiotic_id)

  return HttpResponseDirect(reverse('antibiotics:detail', args=(l.id,)))