from django.shortcuts import render

def home(request):
  context = {}
  return render(request, 'danjaysci/index.html', context)
