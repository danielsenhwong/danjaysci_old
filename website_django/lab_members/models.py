from django.db import models
from datetime import date

# Create your models here.
class LabMember(models.Model):
  # make a list of years since Dan received his PhD
  DAN_PHD_YEAR_LIST = list()
  for y in range(1985, date.today().year):
    DAN_PHD_YEAR_LIST.append( (y, y) )
  # convert the list to a tuple so that this will be valid for the form
  DAN_PHD_YEAR_TUPLE = tuple(DAN_PHD_YEAR_LIST)

  # make a list of trainee types. this may be better suited to be a separate
  # model in the future so we might add new types of trainees.
  TRAINEE_TYPE = (
    ("Post-doctoral Fellow", "Post-doctoral Fellow"),
    ("Graduate Student, PhD", "Graduate Student, PhD"),
    ("Medical Student, MD", "Medical Student, MD"),
    ("Graduate Student, MS", "Graduate Student, MS"),
    ("Technician", "Technician"),
    ("Undergraduate Student (PREP)", "Undergradaute Student (PREP)"),
    ("Undergraduate Student (Full year / Thesis)", "Undergraduate Student (Full year / Thesis)"),
    ("Undergraduate Student (Summer)", "Undergraduate Student (Summer)"),
    ("High School Student", "High School Student"),
    ("Visiting Scientist", "Visiting Scientist"),
  )
  
  first_name = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  trainee_type = models.CharField(
    max_length = 128,
    choices = TRAINEE_TYPE,
    blank = True,
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
    return '%s %s, %s (%i-%i)' % (
      self.first_name, 
      self.last_name,
      self.trainee_type,
      self.start_year,
      self.end_year,
    )

  def name_str(self):
    return '%s %s' % (self.first_name, self.last_name)
  name_str.short_description = 'Name'

  def lab_years(self):
    return '%i - %i' % (self.start_year, self.end_year)
