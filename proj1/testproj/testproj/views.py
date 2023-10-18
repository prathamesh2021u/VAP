#this  is made

from django.http import HttpResponse

from django.shortcuts import render

def index(request):
     params={ 'name': 'prathamesh','place':'baramati' }
     return render(request,'index.html',params)

#def Web1(request):
     #return HttpResponse('Welcome to Web1 <a href="/">Back to home</a>')

def removepunc(request):
     mytext=request.GET.get('text','defult')
     return HttpResponse("remove punction from text")

def analyze(request):

     mytext = request.GET.get('text', 'off')
     mycheck = request.GET.get('mycheck','defult')
     lowcase= request.GET.get('lowcase','defult')
     upcase = request.GET.get('upcase', 'default')
     charlength = request.GET.get('charlength','default')
     punctuation = '''(){}'\/@#$%^&[]!<>'''
     lowercase = '''abcdefghijklmnopqrstuvwxyz'''
     upper = " "
     lower = " "
     analyzed = " "
     ch_length = " "
     if mycheck=="on":
          for char in mytext:
             if char not in punctuation:
               analyzed= analyzed+char
          params = {'purpsose': 'after  remove punctuation', 'analyzer_text': analyzed}
          return render(request, 'analyze.html', params)
     elif lowcase=="on":
          lower=mytext.lower()
          par  ={'purpsose':'after conver into lowercase','analyzer_text':lower}
          return render(request,'analyze.html',par)

     elif upcase == "on":
          upper = mytext.upper()
          par = {'purpsose': 'after convert into uppercase', 'analyzer_text': upper}
          return render(request, 'analyze.html', par)

     elif charlength =="on":
          for char in mytext:
               analyzed= analyzed+char
               totalcount =len(analyzed)
          par = {'purpsose': 'total number of characters', 'analyzer_text':totalcount}
          return render(request, 'analyze.html', par)


     else:
          return ("error no checkboe select")
#analyzed = mytext

#print(mytext)
#print(remvpun)


def uprcase(request):
     return HttpResponse("Text convert into  upercase")

def lawcase(request):
     return HttpResponse("text convert into lawercase")

def charcount(request):
     return HttpResponse("count total no of char")