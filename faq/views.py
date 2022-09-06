from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Question
from .forms import FaqForm


def faq_page(request):
    """ FAQ's page view"""

    questions = Question.objects.all().filter(status=1).order_by('-created_on')
    context = {
        'questions': questions
    }
    template = 'faq/faq.html'

    return render(request, template, context)


@login_required
def add_faq(request):
    """ Form for add questiona and answer """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    questions = Question.objects.all()

    if request.method == 'POST':
        form = FaqForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added FAQ!')
            return redirect(reverse('add_faq'))
        else:
            messages.error(
                request, 'Failed to add FAQ. Please ensure the form is valid.')
    else:
        form = FaqForm()
    template = 'faq/add_faq.html'
    context = {
        'form': form,
        'questions': questions,
        'on_page': True
    }
    return render(request, template, context)