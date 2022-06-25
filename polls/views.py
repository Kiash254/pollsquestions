from audioop import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *


def Indexview(request):
    questions=Questions.objects.order_by('-pub_date')[:5]
    context={
        'questions':questions
    }
    return render(request,'polls/index.html',context)
def Details(request,pk):
    try:
        qui=Questions.objects.get(id=pk)
    except Questions.DoesNotExist:
        raise Http404('questions does not exist')
    context={
        'qui':qui
    }
    return render(request, 'polls/details.html',context)
        
def Results(request,pk):
    qui=get_object_or_404(Questions,id=pk)
    context={
        'qui':qui
    }
    return render(request,'polls/res.html',context)



def Vote(request, pk):
    quiz=get_object_or_404(Questions, id=pk)
    try:
        selected_choice=quiz.choice_all.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        
        return render(request, 'polls/details.html', {
            'quiz':'quiz','error_message':'no question selected'
        ,})
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(quiz.id)))

