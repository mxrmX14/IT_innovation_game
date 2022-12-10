from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def score_keeper(request):
    return render(request, 'score_keeper.html')

def home(request):
    return render(request, 'home.html')

def rules(request):
    return render(request, 'rules.html')