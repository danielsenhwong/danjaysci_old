from django.contrib import admin
from plasmids.models import Plasmid, dnaPrep, SelectionAntibiotic

class PlasmidAdmin(admin.ModelAdmin):
  list_display = (
    '__unicode__',
    'names',
    'antibiotic_resistance',
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
    'names',
  )
  list_editable = (
    'date_received',
    'glycerol_stock_made',
  )
  search_fields = (
    'name',
    'alternate_names',
    'plasmid_source',
    'notes',
  )
  list_filter = (
    'prokaryotic_selection',
    'eukaryotic_selection',
    'plasmid_source',
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
  

class PrepAdmin(admin.ModelAdmin):
  list_display = (
    'plasmid',
    'prep_date',
    'scale',
    'elution_volume_ul',
    'dna_conc',
    'a260_280',
    'location',
    'notes',
  )
  
  search_fields = (
    'plasmid',
    'notes',
  )
  

  
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
admin.site.register(dnaPrep, PrepAdmin)
admin.site.register(SelectionAntibiotic, SelectionAntibioticAdmin)
