from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    htmlStarttag = "<!doctype html>\n<html>"
    headtag = """
        <head>
            <meta name="viewport" content="width=device-width, user-scalable=no" />
            <link rel="manifest" href="manifest.json" />
        </head>
    
    """
    bodytag = """
        <body>
            <h1>Helloe world</h1>
        </body>
    """
    htmlEndtag = "</html>"
    filename = 'www/index.html'
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w+") as f:
        f.write("%s \n %s \n %s \n %s" % (htmlStarttag, headtag, bodytag, htmlEndtag))
        f.close()

    # f= open("index.html","w+")
    
    return HttpResponse("Hello world")