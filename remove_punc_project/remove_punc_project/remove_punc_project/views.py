from string import punctuation
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')
    
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ' '
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
    
    elif(fullcaps == 'on'):
        analyzed = ' '
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Change To UPPERCASE', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', param)
        
    else:
        return HttpResponse("Errors")
