from django.db import models
from datetime import date

# Create your models here.
class LabMember(models.Model):
  # make a list of years since Dan received his PhD
  DAN_PHD_YEAR_LIST = list()
  for y in range(1985, date.today().year + 1):
    DAN_PHD_YEAR_LIST.append( (y, y) )
  # convert the list to a tuple so that this will be valid for the form
  DAN_PHD_YEAR_TUPLE = tuple(DAN_PHD_YEAR_LIST)

  # make a list of trainee types. this may be better suited to be a separate
  # model in the future so we might add new types of trainees.
  TRAINEE_TYPE = (
    ("Post-doctoral Fellow",     "Post-doctoral Fellow"),
    ("Graduate Student, PhD",    "Graduate Student, PhD"),
    ("Medical Student, MD",      "Medical Student, MD"),
    ("Graduate Student, MS/MBS", "Graduate Student, MS/MBS"),
    ("Technician",               "Technician"),
    ("PREP Scholar",             "PREP Scholar"),
    ("Undergraduate Student",    "Undergraduate Student"),
    ("High School Student",      "High School Student"),
    ("Visiting Scientist",       "Visiting Scientist"),
  )
  
  first_name = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  trainee_type = models.ForeignKey(
    'TraineeType'
  )
  start_year = models.PositiveIntegerField(
    choices = DAN_PHD_YEAR_TUPLE,
    blank = True,
    null = True,
  )
  end_year = models.PositiveIntegerField(
    choices = DAN_PHD_YEAR_TUPLE,
    blank = True,
    null = True,
  )
  current_position = models.TextField(
    blank = True,
    null = True,
  )
  date_added = models.DateField(
    auto_now_add = True,
  )
  last_updated = models.DateField(
    help_text = 'The date this person\'s "Current Position" information was last updated.',
    blank = True,
    null = True,
  )

  def __unicode__(self):
    output = '%s %s, %s (%d' % (
      self.first_name,
      self.last_name,
      self.trainee_type,
      self.start_year
    )
    
    if not self.end_year:
      output += '-present)'
    elif self.end_year == self.start_year:
      output += ')'
    else:
      output += '-%d)' % (self.end_year)
    return output

  def name_str(self):
    output = '%s%s%s' % (self.first_name, unichr(160), self.last_name)
    return output
  name_str.short_description = 'Name'

  def lab_years(self):
    output = '%d' % (self.start_year)
    
    if not self.end_year:
      output += '-present'
    elif self.end_year == self.start_year:
      output += ''
    else:
      output += '-%d' % (self.end_year)
    return output

class TraineeType(models.Model):
  name = models.CharField(
    max_length = 64,
  )
  abbreviation  = models.CharField(
    max_length = 24,
  )
  description = models.TextField(
    blank = True,
    null = True,
  )
  
  def __unicode__(self):
    output = "%s" % (self.name)
    
    return output
  