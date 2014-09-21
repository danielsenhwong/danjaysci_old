from django.contrib import admin
from plasmids.models import Plasmid, dnaPrep, SelectionAntibiotic

# Register your models here.
admin.site.register(Plasmid)
admin.site.register(dnaPrep)
admin.site.register(SelectionAntibiotic)
