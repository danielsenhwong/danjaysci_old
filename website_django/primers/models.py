from django.db import models

class Primer(models.Model):
  number = models.PositiveIntegerField(unique=True)
  name = models.CharField(max_length=30) # set to IDTdna maximum allowed length
  sequence = models.TextField(
    blank = True, 
    null = True, 
    help_text = "Please enter the sequence of the primer/oligo you have designed. It is OK to hold numbers while you are designing the specific sequence, so this field can be blank.",
  )
  notes = models.TextField(
    blank = True,
    null = True,
    help_text = "Please add notes on the usage and application of this oligo, e.g. annealing temperature, intended use, etc.",
  )
  vendor = models.CharField(
    max_length = 64,
    help_text = "Where was this primer ordered? Leave this blank if it hasn't been ordered yet.",
    blank = True,
    null = True,
  )
  order_num = models.CharField(
    max_length = 64,
    help_text = "What is the order number associated with this primer? Enter the primer as a new one if you are re-ordering an old one. Leave this blank if it hasn't been ordered yet.",
    blank = True,
    null = True,
  )
  ref_num = models.CharField(
    max_length = 64,
    help_text = "Is there a manufacturer-associated reference number? If so, enter that here.",
    blank = True,
    null = True,
  )
  mfg_id = models.CharField(
    max_length = 64,
    help_text = "Manufacturing ID?",
    blank = True,
    null = True,
  )
  date_ordered = models.DateField(
    blank = True,
    null = True,
    help_text = "Date ordered. Format: YYYY-MM-DD. Leave blank if not yet ordered.",
  )
  user_id = models.PositiveIntegerField() # switch this to ForeignKey() later
  datasheet = models.FileField(
    blank = True,
    null = True,
  )

  def __unicode__(self): # Python 3: def __str__(self):
    return "%i - %s (%i nt)" % (
      self.number,
      self.name,
      len(self.sequence.replace(' ', '')),
    )
