from django.contrib import admin
from plasmids.models import Plasmid, dnaPrep, SelectionAntibiotic

class SelectionAntibioticAdmin(admin.ModelAdmin):
  list_display = (
    'name',
    'resistance_gene',
    'prokaryotic_use',
    'eukaryotic_use',
  )

# Register your models here.
admin.site.register(Plasmid)
admin.site.register(dnaPrep)
admin.site.register(SelectionAntibiotic, SelectionAntibioticAdmin)
