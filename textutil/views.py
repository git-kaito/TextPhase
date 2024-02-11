#self-made
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char
        params = {'purpose' : 'Removed Punctuations', 'analyzed_text' : analyzed}
        djtext = analyzed
    if (fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose' : 'Capitalized Text ', 'analyzed_text' : analyzed}
        djtext = analyzed
    if(newlineremove == "on"):
        analyzed=""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed+char
        params = {'purpose' : 'Removed New LInes', 'analyzed_text' : analyzed}
        djtext = analyzed
    if(charcount == "on"):
        analyzed = ""
        for char in djtext:
            analyzed= len(djtext)
        params = {'purpose' : 'Character Count', 'analyzed_text' : analyzed}
        djtext = analyzed
    if(extraspaceremover =="on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1]) == " ":
                analyzed = analyzed+char
        params = {'purpose' : 'Removed New LInes', 'analyzed_text' : analyzed}
        djtext = analyzed
    if(extraspaceremover!="on" and charcount!="on" and newlineremove!="on" and fullcaps!="on" and removepunc!="on"):
        return HttpResponse('Please Choose any of the given options.')
    return render(request,'analyze.html', params)