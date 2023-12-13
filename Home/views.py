from django.http import response
from django.shortcuts import render, HttpResponse, redirect
import requests
from datetime import datetime
from Home.models import SearchQ
from contentAPI import getContent
from django.template.loader import render_to_string
import os
from checkDB import getPage

# Assuming you have the 'query' and 'content' variables available



def home(request):
    
    return render(request, 'home.html')
    #return HttpResponse('This is an HTTP Response')

def about(request):
    return render(request, 'abt.html')
    #return HttpResponse('This is an HTTP Response')

def app1(request):
    return render(request, 'app1.html')
    #return HttpResponse('This is an HTTP Response')


def search(request):
    
    if request.method == "POST":
        query = request.POST.get('queryText')
        query = query.lower()
        print("Recieved query is : ", query)
        if query != "":
            content4 = getPage(query=query)
            print("content4 is: ",content4)
            if content4 != "No Articles":
                dateTime1 = datetime.today()
                id1 = datetime.now()
                id2 = int(id1.timestamp())
                info = SearchQ(id2,query,dateTime1)
                info.save()
                print(content4)
                goTo = query + ".html"
                context = {
                "Queried": query
                }
                return render(request,goTo,context)
                
            else:
                print(content4)
                return render(request,'tmkoc.html')
        else:
            context = {
            "titlez" : "Search for a topic",
            "Content": "Get an AI generated article according to the search",
            "imgUrl": "/static/type.jpg"
            }
            return render(request,'search.html', context)
        
    else:
        context = {
        "titlez" : "Search for a topic",
        "Content": "Get an AI generated article according to the search",
        "imgUrl": "/static/type.jpg"
        }
        return render(request,'search.html', context)
    #Use Redis
