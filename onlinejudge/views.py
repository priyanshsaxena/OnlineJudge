from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from .forms import SubmissionForm

from .models import User, Question, Submission
from .func import run_file

# Create your views here.

def index(request):
    return render(request, 'onlinejudge/index.html')

def problems(request):
	latest_problems_list = Question.objects.all()[:5]
	template = loader.get_template('onlinejudge/problems.html')
	context = {
		'latest_problems_list': latest_problems_list,
	}
	return HttpResponse(template.render(context, request))

def problem_details(request, problem_name):
	problem = get_object_or_404(Question, question_name=problem_name)
	template = loader.get_template('onlinejudge/details.html')
	context = {
		'problem': problem,
	}
	return HttpResponse(template.render(context, request))

def new_submission(request):
	if request.method == 'POST' and request.FILES['codefile']:
		submission_number = Submission.objects.last().id + 1
		run_file(request.FILES['codefile'])
		template = loader.get_template('onlinejudge/submitted.html')
		context = {
			'submission_number': submission_number,
		}
		return HttpResponse(template.render(context, request))
	else:
		return HttpResponseRedirect(reverse('onlinejudge:problems'))