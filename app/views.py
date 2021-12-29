import random
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, DetailView

from app.models import Question, Answer


class HomePageView(TemplateView):
    template_name = 'app/home.html'


class HowToView(TemplateView):
    template_name = 'app/howto.html'


class TestView(DetailView):
    model = Question

    def dispatch(self, request, *args, **kwargs):
        self.object = Question.objects.filter(difficulty=self.kwargs['difficulty']).order_by('?')[:1]

        return super(TestView, self).dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(self.object)

    def post(self, request, **kwargs):
        choice = request.POST.get('choice')
        answer = Answer.objects.get(id=choice)
        if answer.correct:
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
    context = super(AboutView, self).get_context_data(**kwargs)
    ad = random.choice([('2', '1'), ('2', 'sqrt(2)'), ('', '1'), ('', '0'), ('2', 'sqrt(3)')])
    f = random.choice(['sin', 'cos'])
    c = random.randint(0, 10)
    b = random.randint(0, 10)
    context['equation'] = '\[' + ad[0] + f + ' (' + b + 'x + ' + c + ') = ' + ad[1] + '\]'
    return context
