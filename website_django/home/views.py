from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.conf import settings
from pyzotero import zotero

# Create your views here.

def index(request):
  return render_to_response('index.html', context_instance=RequestContext(request))

def references(request, starting_item='0'):
  # open a connection to the lab Zotero library
  zot = zotero.Zotero(settings.ZOTERO_LIBRARY_ID, settings.ZOTERO_LIBRARY_TYPE, settings.ZOTERO_API_KEY)
  
  # make a list of the collections belonging to the lab and their keys
  collections = {'CALI': 'DRGQSTRD',
                 
                }
  
  # get the size of the CALI collection, and calculate the index of the first reference
  # also make a list of offset values
  collection_size = zot.num_collectionitems(collections['CALI'])
  reference_index = collection_size - int(starting_item)
  offset_list = range(0, collection_size, 50)
  
  # read references from the CALI collection, 50 items at a time, starting from the most 
  # recent, or some arbitrary offset
  items = zot.collection_items(collections['CALI'],
                               start=starting_item, 
                              )
  
  # render HTML output using the references template, and also make some variables 
  # available for use in the template
  return render(request, 'references.html', {'items': items,
                                             'collection_size': collection_size,
                                             'reference_index': reference_index,
                                             'offset_list': offset_list,
                                            })

