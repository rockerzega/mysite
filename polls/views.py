from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect #, Http404
#from django.template import RequestContext, loader
from django.urls import reverse

from .models import Choice, Question

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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #Redibuja la pregunta votada en el formulario
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "No ha escogido una opción.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre retorna un HttpResponseRedirect luego de una peticion exitosa
        # con datos de POST. Esto evita que los datos se publiquen dos veces si un
        # usuario presiona el boton de retroceso
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

#view que permite ver las ultimas 5 publicaciones sepradas con una coma 
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)