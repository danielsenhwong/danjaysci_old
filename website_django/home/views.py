from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.conf import settings
from pyzotero import zotero

# Create your views here.

def index(request):
  return render_to_response('index.html', context_instance=RequestContext(request))

def references(request, starting_item=0, order_by="date", sort_type="desc"):
  # open a connection to the lab Zotero library
  zot = zotero.Zotero(settings.ZOTERO_LIBRARY_ID, settings.ZOTERO_LIBRARY_TYPE, settings.ZOTERO_API_KEY)
  
  collections = {'CALI': 'DRGQSTRD',
                 
                }
  
  # get the size of the CALI collection
  collection_size = zot.num_collectionitems(collections['CALI'])
  
  # grab everything from the CALI collection, 50 items at a time
  items = zot.collection_items(collections['CALI'], start=starting_item, limit=50, order=order_by, sort=sort_type)
  
  return render(request, 'references.html', {'items': items,
                                             'collection_size': collection_size,
                                             
                                            })

