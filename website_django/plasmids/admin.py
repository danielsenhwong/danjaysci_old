from django.contrib import admin
from plasmids.models import Plasmid, dnaPrep, SelectionAntibiotic

class PlasmidAdmin(admin.ModelAdmin):
  list_display = (
    '__unicode__',
    'name',
    'alternate_names',
    'prokaryotic_selection',
    'eukaryotic_selection',
    'size_kb',
    'parent_plasmid',
    'plasmid_source',
    'date_received',
    'glycerol_stock_made',
    'datasheet',
    'notes',
  )
  list_display_links = (
    '__unicode__',
    'name',
  )
  list_editable = (
    'date_received',
    'glycerol_stock_made',
  )
  search_fields = (
    'name',
    'alternate_names',
    'notes',
  )
  list_filter = (
    'prokaryotic_selection',
    'eukaryotic_selection',
  )
  ordering = (
    'number',
  )
  fieldsets = [
    ('Primary Information',	   {'fields': [
                                           'number',
                                           'name',
                                           'alternate_names',
                                           'size_kb',
                                           'date_received',
                                           'glycerol_stock_made',
                                           'plasmid_source',
                                           'datasheet',
                                           'notes',
                                          ]}),
    ('Biological information', {'fields': [
                                           'prokaryotic_selection',
                                           'eukaryotic_selection',
                                           'parent_plasmid',
                                           'clones',
                                          ]}),
  ]
  
  
class SelectionAntibioticAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'resistance_gene',
    'prokaryotic_use',
    'eukaryotic_use',
  )
  search_fields = (
    'name',
  )
  list_filter = (
    'prokaryotic_use',
    'eukaryotic_use',
    
  )
  
# Register your models here.
admin.site.register(Plasmid, PlasmidAdmin)
admin.site.register(dnaPrep)
admin.site.register(SelectionAntibiotic, SelectionAntibioticAdmin)
