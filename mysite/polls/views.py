from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Person

def index(request):
        people = Person.objects.all()
        context = {'people': people}
        # my_objects = MyModel.objects.all()
        return render(request, 'index.html', context)
        # return HttpResponse("Hello World. Welcome to my Site :)")

# def create_person(request):
#         if request.method == 'POST':
#                 form = PersonForm(request.POST)
#                 if form.is_valid():
#                         name = form.cleaned_data['name']
#                         age = form.cleaned_data['age']
#                         person = Person(name=name, age=age)
#                         person.save()
#                         return redirect('person_list')
#                 else:
#                         form = PersonForm()
#                 return render(request, 'create_person.html', {'form': form})