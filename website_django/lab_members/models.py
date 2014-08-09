from django.db import models
from datetime import date

# Create your models here.
class LabMember(models.Model):
  # make a list of years since Dan received his PhD
  DAN_PHD_YEAR_LIST = [[]]
  for y in range(1985, date.today().year):
    DAN_PHD_YEAR_LIST.append([y,  y])
  TRAINEE_TYPE = (
    ("", ""),
    ("Post-doctoral Fellow", "Post-doctoral Fellow"),
    ("Graduate Student, PhD", "Graduate Student, PhD"),
    ("Medical Student, MD", "Medical Student, MD"),
    ("Graduate Student, MS", "Graduate Student, MS"),
    ("Technician", "Technician"),
    ("Undergraduate Student (PREP)", "Undergradaute Student (PREP)"),
    ("Undergraduate Student", "Undergraduate Student"),
    ("Summer Undergraduate Student", "Summer Undergraduate Student"),
    ("High School Student", "High School Student"),
    ("Visiting Scientist", "Visiting Scientist"),
  )
  
  first_name = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  start_year = models.PositiveIntegerField(
    choices = DAN_PHD_YEAR_LIST,
    blank = True,
    null = True,
  )
  end_year = models.PositiveIntegerField(
    choices = DAN_PHD_YEAR_LIST,
    blank = True,
    null = True,
  )
  current_position = models.TextField(
    blank = True,
    null = True,
  )
