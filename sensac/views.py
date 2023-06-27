# from django.http import HttpResponse

from django.shortcuts import redirect, render

from .forms import ContactoForm, NewsletterForm
from .models import Produto, Servicos


def home(request):
    if request.method == 'POST':
        contacto_form = ContactoForm(request.POST)
        newsletter_form = NewsletterForm(request.POST)

        if contacto_form.is_valid():
            contacto_form.save()

        if newsletter_form.is_valid():
            newsletter_form.save()

        # Redirecionar para a página inicial após salvar os formulários
        return redirect('home')

    else:
        contacto_form = ContactoForm()
        newsletter_form = NewsletterForm()

    servicos = Servicos.objects.all()
    produtos = Produto.objects.all()

    context = {
        'servicos': servicos,
        'produtos': produtos,
        'contacto_form': contacto_form,
        'newsletter_form': newsletter_form
    }

    return render(request, 'sensac/page/home.html', context)
