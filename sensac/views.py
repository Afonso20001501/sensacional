# from django.http import HttpResponse


from django.shortcuts import render

from .forms import ContactoForm, NewsletterForm
from .models import Produto, Servicos


# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactoForm()
        return render(request, 'sensac/page/home.html', {'form': form})

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NewsletterForm()
        return render(request, 'sensac/page/home.html', {'form': form})

    servicos = Servicos.objects.all()
    produtos = Produto.objects.all()

    context = {
        'servicos': servicos,
        'produtos': produtos
    }

    return render(request, 'sensac/page/home.html', context)
