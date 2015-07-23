from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.ListView) :
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def foo(request):
    context={'some_text':"Here are some words"}
    return render(request, 'polls/foo.html',context)


def vote(request, question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) :

        return render(request, 'polls/detail.html', {
            'question':p,'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


