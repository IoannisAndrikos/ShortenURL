from django.shortcuts import render
from .forms import getURL
from .callAPIs import culltyShorten


def ShortenURL(request):
        form = getURL()
        context ={}
        context['form']= form
        context['short_url']= ''

        if request.method == 'POST':
            form = getURL(request.POST)
            if form.is_valid():
                if request.POST.get('click_shorten'):
                    context['short_url'] = culltyShorten(form.cleaned_data['text_url'])

        return render(request,"shortenURL.html",  context)