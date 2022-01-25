from string import punctuation
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def analyze(request):
    djtext = request.POST.get('text', 'default')
    
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')

    if removepunc == 'on':
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ' '
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        param = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', param)
    
    if(fullcaps == 'on'):
        analyzed = ' '
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Change To UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', param)
    
    if(newlineremover == 'on'):
        analyzed = ' '
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        
        param = {'purpose': 'Remove New Line', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")
    else:
        return render(request, 'analyze.html',param)
