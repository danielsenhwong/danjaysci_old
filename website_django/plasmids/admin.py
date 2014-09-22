from django.contrib import admin
from plasmids.models import Plasmid, dnaPrep, SelectionAntibiotic

class PlasmidAdmin(admin.ModelAdmin):
  list_display = (
    'number',
    'name',
    'prokaryotic_selection',
    'eukaryotic_selection',
    'size',
    'parent_plasmid',
  )

class SelectionAntibioticAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'resistance_gene',
    'prokaryotic_use',
    'eukaryotic_use',
  )

# Register your models here.
admin.site.register(Plasmid, PlasmidAdmin)
admin.site.register(dnaPrep)
admin.site.register(SelectionAntibiotic, SelectionAntibioticAdmin)
