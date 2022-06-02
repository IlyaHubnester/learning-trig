import random
import math
import json
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView
from django.http import HttpResponse

from app.models import Question, Answer


def generate_simple():
    functions = {'cos': math.acos, 'sin':math.asin, 'tg':math.atan}
    f = random.choice(list(functions.keys()))
    a = "{:.2f}".format(random.uniform(-1,1))
    solution = functions[f](float(a))
    return {"equation": "\[ "+ f + " x = " + a + " \]", "solution": "{:.2f}".format(solution)}

def generate_odnorodn():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    solution = math.atan(-(b/a))
    return {"equation": "\[ "+ str(a) + " sin x + " + str(b) + " cos x = 0 \]", "solution": "{:.2f}".format(solution)}


def generate_quadratic():
    while True:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        d = random.randint(1, 10)
        discr = b**2 - 4 * a * d
        if discr >= 0:
            break
    solution = math.atan((-b + math.sqrt(b**2-4*a*d))/2*a)
    return {"equation": "\[ "+ str(a) + " sin^2 x + " + str(b) + " sin x cos x + " + str(d) + "cos^2 x  = 0 \]", "solution": "{:.2f}".format(solution)}


def generate_simple_view(request):
    return HttpResponse(json.dumps(generate_simple()))

def generate_odnorodn_view(request):
    return HttpResponse(json.dumps(generate_odnorodn()))

def generate_quadratic_view(request):
    return HttpResponse(json.dumps(generate_quadratic()))

class HomePageView(TemplateView):
    template_name = 'app/home.html'


class HowToView(TemplateView):
    template_name = 'app/howto.html'

class HowTo2View(TemplateView):
    template_name = 'app/howto2.html'

class HowTo3View(TemplateView):
    template_name = 'app/howto3.html'

class TestView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        if self.kwargs['difficulty'] == 0:
            self.question = generate_simple()
        if self.kwargs['difficulty'] == 1:
            self.question = generate_odnorodn()
        if self.kwargs['difficulty'] == 2:
            self.question = generate_quadratic()
        return super(TestView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['equation'] = self.question['equation']
        context['solution'] = self.question['solution']
        return context

    def post(self, request, **kwargs):
        answer = request.POST.get('answer')
        solution = request.POST.get('solution')
        if answer == solution:
            return redirect('right', difficulty=self.kwargs['difficulty'])
        else:
            return redirect('wrong', difficulty=self.kwargs['difficulty'])

    template_name = 'app/test.html'


class TestRightView(TemplateView):
    template_name = 'app/right.html'


class TestWrongView(TemplateView):
    template_name = 'app/wrong.html'


class TestRandomView(TemplateView):
    template_name = 'app/random.html'

    def get_context_data(self, **kwargs):
        context = super(TestRandomView, self).get_context_data(**kwargs)
        ad = random.choice([('2', '1'), ('2', '\sqrt{2}'), ('', '1'), ('', '0'), ('2', '\sqrt{3}')])
        f = random.choice(['sin', 'cos'])
        c = random.randint(1, 10)
        b = random.randint(1, 10)
        context['equation'] = '\[' + ad[0] + f + ' (' + str(b) + 'x + ' + str(c) + ') = ' + ad[1] + '\]'
        return context
