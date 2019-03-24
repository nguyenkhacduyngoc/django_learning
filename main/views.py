from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question
from django.template import loader
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('main/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'main/index.html', context)
    # return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question does not exist')
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'main/detail.html', {'question': question})
    # return HttpResponse('detail %s.' % question_id)

def results(request, question_id):
    response = "result %s."
    
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('vote %s.' % question_id)