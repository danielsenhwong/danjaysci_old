from django.contrib import admin
from lab_members.models import LabMember

class LabMemberAdmin(admin.ModelAdmin):
  exclude = ('date_added',)
  
  fieldsets = [
    ('Biographical information',   {'fields': ( ('first_name', 'last_name',), )}),
    ('Lab-related information',    {'fields': (
                                     'trainee_type',
                                      ('start_year', 'end_year',),
                                   )}),
    ('Career-related information', {'fields': ('current_position',)}),
    ('Administrative information', {
                                     'classes': ('collapse',), # actually not necessary to hide?
                                     'fields': ('last_updated',)
                                   }),
  ]

  list_display = (
    'name_str',
    'trainee_type',
    'lab_years',
    'current_position',
    'date_added',
    'last_updated',
  )

  list_filter = ['trainee_type', 'start_year', 'end_year']

  search_fields = ['first_name', 'last_name', 'current_position', 'trainee_type']

  # may want to add filter_horizontal for trainee_type
  #filter_horizontal = ['trainee_type']

# Register your models here.
admin.site.register(LabMember, LabMemberAdmin)
