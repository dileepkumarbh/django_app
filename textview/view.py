#self created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return render(request, "index.html")

def about(request):
    return HttpResponse("about")

def anasyze(request):
    #get text from template textarea
    user_text=(request.GET.get('text', 'default'))
    chek_box=(request.GET.get('removepunc','off'))
    chek_space=(request.GET.get('removespace','off'))
    print(chek_box)
    print(chek_space)
    print(user_text)

    #analyze the text
    puncuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    anasyzed =""
    if chek_box=='on':
        for char in user_text:
            if char not in puncuations:
                anasyzed = anasyzed+char

    else:
        return HttpResponse('error')
    perams = {'purpose': "remove punchuations", 'analyzed_text': anasyzed}
    return render(request, 'analyze.html', perams)

def charupper(request):
    return HttpResponse("charupper")