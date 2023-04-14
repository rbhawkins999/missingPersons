from django.shortcuts import render
from .models import Person

# Create your views here.
def indexPageView(request) :
    return render(request, 'persons/index.html')

def tablePageView(request) :
    db_person = Person.objects.all()

    context = {
        "data" : db_person
    }
    return render(request, 'persons/table.html', context)

def showPersonPageView(request, id) :
    person = Person.objects.get(id=id)

    context= {
        "data" : person
    }

    return render(request, 'persons/showPerson.html', context)


# def displayPersonPageView(request, id) :
#     person = Person.objects.get(id=id)

#     context= {
#         "data" : person
#     }

#     return render(request, 'persons/showPerson.html', context)
