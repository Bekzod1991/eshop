from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    university = 'Milliy Universitet'
    department = 'Programming Engineering'
    context = {'university': university, 'department': department}
    return render(request, 'index.html', context)