from django.shortcuts import render

# Create your views here.
def primaryschoolhome(request):
    return render(request,'primary/home.html')
