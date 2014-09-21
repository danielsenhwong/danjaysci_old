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

  number = models.CharField(
    max_length = 9,
  )
  name = models.CharField(
    max_length = 64
  )
  alternate_names = models.TextField(
    blank = True,
    null = True,
  )
  antibiotic_selection = models.ForeignKey(
    'SelectionAntibiotic',
    on_delete = models.PROTECT, # do not allow antibiotic to be deleted from database if a dependent plasmid is also in the database
  )
  size_kb = models.DecimalField(
    max_digits = 4,
    decimal_places = 2,
    verbose_name = "Size (kb)",
  )
  date_received = models.DateField()
  datasheet = models.FileField(
    blank = True,
    null = True,
  )
  received_from = models.CharField(
    max_length = 128,
  )
  notes = models.TextField(
    blank = True,
    null = True,
  )
  glycerol_stock_made = models.DateField(
    blank = True,
    null = True,
  )
  clones = models.CharField(
    max_length = 24,
    blank = True,
    null = True,
  )
  
  def __unicode__(self):
    output = '(%s) %s' % (
      self.number,
      self.name,
    )
    
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

class SelectionAntibiotic(models.Model):
  name = models.CharField(
    max_length = 64,
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
  )
  
  def __unicode__(self):
    output = '%s' % (self.name)
    
    return output