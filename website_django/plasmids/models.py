from django.db import models
from datetime import date

# Create your models here.

class Plasmid(models.Model):
  ANTIBIOTICS = (
    ("Ampicillin",   "AmpR"),
    ("Blasticidin",  "bsr/bsd"),
    ("Hygromycin B", "hyg/hph"),
    ("Kanamycin",    "KanR"),
    ("Neomycin/G418","NeoR"),
    ("Puromycin",    "PuroR/pac"),
    ("Zeocin",       "ZeoR/Sh ble"),
  )

  number = models.IntegerField(
    max_length = 8,
    help_text = "Plasmids will be automatically given a 'p' prefix, e.g. p1, p2, p3, etc.",
    unique = True,
  )
  name = models.CharField(
    max_length = 64,
  )
  alternate_names = models.CharField(
    max_length = 64,
    blank = True,
    null = True,
  )
  prokaryotic_selection = models.ForeignKey(
    'SelectionAntibiotic',
    limit_choices_to = {
      'prokaryotic_use': True,
    },
    related_name = 'prokaryotic_antibiotic',
    on_delete = models.PROTECT, # do not allow antibiotic to be deleted from database if a dependent plasmid is also in the database
  )
  eukaryotic_selection = models.ForeignKey(
    'SelectionAntibiotic',
    limit_choices_to = {
      'eukaryotic_use': True,
    },
    related_name = 'eukaryotic_antibiotic',
    on_delete = models.PROTECT, # do not allow antibiotic to be deleted from database if a dependent plasmid is also in the database
    blank = True,
    null = True,
  )
  size_kb = models.DecimalField(
    max_digits = 4,
    decimal_places = 2,
    verbose_name = "Size (kb)",
  )
  date_received = models.DateField(
    help_text = "Date the plasmid was received or generated.",
  )
  datasheet = models.FileField(
    blank = True,
    null = True,
  )
  plasmid_source = models.CharField(
    max_length = 128,
    help_text = "The person, organization, or company the plasmid was received from or made by.",
  )
  parent_plasmid = models.ForeignKey(
    'Plasmid',
    on_delete = models.PROTECT,
    blank = True,
    null = True,
    help_text = 'Identity of the vector. Insert information should be added in the "Notes" field.',
  )
  notes = models.TextField(
    blank = True,
    null = True,
    help_text = 'Supplier catalog number, insert cloning details, and all other relevant information should be recorded here.',
  )
  glycerol_stock_made = models.DateField(
    blank = True,
    null = True,
  )
  clones = models.CharField(
    max_length = 24,
    blank = True,
    null = True,
    help_text = 'A comma-separated list of clone designations, e.g. A, B, C, etc.',
  )
  
  def __unicode__(self):
    output = 'p%s' % (
      self.number,
    )
    return output
  
  def name_str(self):
    output = 'p%s - %s' % (
      self.number,
      self.name,
    )
    return output
    
  def names(self):
    output = '%s' % (
      self.name,
    )
    if self.alternate_names:
      output += '\n(%s)' % (
        self.alternate_names,
      )
    return output
    
  def antibiotic_resistance(self):
    output = '(Pro) %s' % (
      self.prokaryotic_selection,
    )
    if self.eukaryotic_selection:
      output += ', (Eu) %s' % (
        self.eukaryotic_selection,
      )
    return output
    
  def glycerol_status(self):
    if self.glycerol_stock_made:
      output = True
    else:
      output = False
    return output

class dnaPrep(models.Model):
  PREP_SCALE = (
    ("mini, ~20 ug DNA", "mini"),
    ("midi, ~200 ug DNA", "midi"),
    ("maxi, ~1000 ug DNA", "maxi"),
    ("mega, ~2500 ug DNA", "mega"),
    ("giga, ~10000 ug DNA", "giga"),
  )

  plasmid = models.ForeignKey(
    'Plasmid',
    on_delete = models.PROTECT,  # not allowed to delete parent object with child dnaPreps
  )
  prep_date = models.DateField()
  prep_by = models.CharField(  # convert this to ForeignKey in the future
    max_length = 64,
  )
  scale = models.CharField(
    max_length = 12,
    choices = PREP_SCALE,
  )
  elution_volume_ul = models.IntegerField(
    max_length = 8,
    verbose_name = "Elution volume, uL",
  )
  dna_conc = models.DecimalField(
    max_digits = 8,
    decimal_places = 2,
    verbose_name = "[DNA], ng/uL",
  )
  a260_280 = models.DecimalField(
    max_digits = 5,
    decimal_places = 2,
    verbose_name = "A260/280",
  )
  a260_230 = models.DecimalField(
    max_digits = 5,
    decimal_places = 2,
    verbose_name = "A260/230",
  )
  location = models.CharField(
    max_length = 128,
  )
  notes = models.TextField(
    blank = True,
    null = True,
  )
  depleted = models.BooleanField(
    default = None,
  )

  class Meta:
    verbose_name = "DNA prep"
  
  def __unicode__(self):
    output = '%s, %s %d uL @ %d ng/uL' % (
      self.plasmid,
      self.prep_date,
      self.elution_volume_ul,
      self.dna_conc,
    )
    
    if self.depleted:
      output += " (depleted)"
    
    return output
    
  def dna_conc_str(self):
    output = '%d ng/uL' % (
      self.dna_conc,
    )

class SelectionAntibiotic(models.Model):
  name = models.CharField(
    max_length = 64,
    unique = True,
  )
  resistance_gene = models.CharField(
    max_length = 64,
  )
  prokaryotic_use = models.BooleanField(
    default = None,
  )
  eukaryotic_use = models.BooleanField(
    default = None,
  )
  notes = models.TextField(
    blank = True,
    null = True,
    help_text = "Put recommended working concentration values here."
  )
  
  def __unicode__(self):
    output = '%s' % (self.name)
    
    return output