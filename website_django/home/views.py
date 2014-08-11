from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.conf import settings
from pyzotero import zotero

# Create your views here.

def index(request):
  return render_to_response('index.html', context_instance=RequestContext(request))

def references(request):
  # open a connection to the lab Zotero library
  zot = zotero.Zotero(settings.ZOTERO_LIBRARY_ID, settings.ZOTERO_LIBRARY_TYPE, settings.ZOTERO_API_KEY)
  # grab everything from the CALI library
  
  items = zot.collection_items('DRGQSTRD', order='date')
  
  return render(request, 'references.html', {'items': items})

