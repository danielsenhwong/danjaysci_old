from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic

from lab_members.models import LabMember

# Create your views here.
class IndexView(generic.ListView):
  template_name = 'lab_members/index.html'
  context_object_name = 'latest_lab_member_list'

  def get_queryset(self):
    """Return the last 50 lab members."""
    return LabMember.object.order_by('-start_year')[:50]

class DetailView(generic.DetailView):
  model = LabMember
  tempalte_name = 'lab_member/detail.html'

def edit(request, lab_member_id):
  l = get_object_or_404(LabMember, pk=lab_member_id)

  return HttpResponseDirect(reverse('lab_members:detail', args=(l.id,)))
