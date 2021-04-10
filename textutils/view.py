# i have create file - manthan
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    dtext=request.POST.get('text', 'defult')


    removepuc=request.POST.get('removepunc', 'off')
    callupper=request.POST.get('callupper', 'off')
    newlineremove=request.POST.get('newlineremove', 'off')
    extraspaceremove=request.POST.get('extraspaceremove', 'off')
    charcounter=request.POST.get('charcounter', 'off')


    print(removepuc)
    print(dtext)




    if (removepuc=="on"):
        punctuation = '''!@#$%^&*(){}[]:<>?.,'''
        analyzed = ''
        for char in dtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'removed punctuation', 'analyed_text': analyzed}
        dtext = analyzed
        #return render(request, 'analyze.html', params)




    if(callupper=="on"):
        analyzed=''
        for char in dtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change to uppercase', 'analyed_text': analyzed}
        dtext = analyzed
        #return render(request, 'analyze.html', params)

    if(newlineremove=='on'):
        analyzed = ''
        for char in dtext:
            if char != "\n" and char != '\r':
                analyzed = analyzed + char
        params = {'purpose': 'new line remover', 'analyed_text': analyzed}
        dtext = analyzed
        #return render(request, 'analyze.html', params)


    if(extraspaceremove=='on'):

        analyzed = ''
        for index,char in enumerate(dtext):
            if dtext[index]==" " and dtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'new line remover', 'analyed_text': analyzed}
        dtext = analyzed
        #return render(request, 'analyze.html', params)


    if (charcounter == 'on'):
        analyzed = 0
        for char in dtext:
            analyzed = analyzed+1

        params = {'purpose': 'new line remover', 'analyed_text': analyzed}
        dtext = analyzed
        #return render(request, 'analyze.html', params)

    if(removepuc != "on" and callupper != "on" and newlineremove != 'on' and extraspaceremove !='on' and charcounter != 'on' ):
        return HttpResponse("please select any option and try again!")
    return render(request, 'analyze.html', params)


