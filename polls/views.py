from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse #, Http404
#from django.template import RequestContext, loader
from .models import Question

# Create your views here.
#def index(request):
#    return HttpResponse("Hola. Estas en el incio de la página.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #return HttpResponse("Estas mirando la pregunta %s." % question_id)

"""def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})"""

def results(request, question_id):
    response = "Estas mirando la respuesta ala pregunta %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("Estas votando por la pregunta %s." % question_id)

#view que permite ver las ultimas 5 publicaciones sepradas con una coma 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)