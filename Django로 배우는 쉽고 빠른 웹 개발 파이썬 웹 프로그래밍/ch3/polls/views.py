from django.shortcuts import render

# Create your views here.

# 함수형 뷰

# from django.shortcuts import get_object_or_404, render
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from polls.models import Choice, Question
#
# def index(request):
#     latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, 'polls/detail.html', {'question':question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html',{
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     return render(request, 'polls/results.html', {'question': question})

# import logging
#
# logger = logging.getLogger('mylogger')
#
# def my_view(request, arg1, arg):
#     if bad_mojo:
#         logger.error("Someting went worong")

# 클래스형 뷰

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from polls.models import Choice, Question
import logging

logger = logging.getLogger(__name__)

#--- Class-based GeneriicView
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """최근 생성된 질문 5개를 반환함"""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

#--- Fundtion-based View
def vote(request, question_id):
    logger.debug("vote().question_id: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))