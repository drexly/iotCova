# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import pyrebase
# Create your views here.
from django.http import HttpResponse
#import urllib
#import requests
import datetime
config = {
  "apiKey": "AIzaSyDwL6FPybGvHY4Qiw4e7XvMov4smaevYdw",
  "authDomain": "cova-e7bad.firebaseapp.com",
  "databaseURL": "https://cova-e7bad.firebaseio.com",
  "storageBucket": "cova-e7bad.appspot.com"
}
firebase = pyrebase.initialize_app(config)
status=None
#status='sos'
db = firebase.database()
def index(request,x,y,z):
    #page = urllib.urlopen("https://cova-e7bad.firebaseapp.com/pn.html")
    #src=str(page.read())
    #page.close()
    #page =requests.get("http://cova-e7bad.firebaseapp.com/pn.html")
    #src=str(page)
    lat=float(y)
    lng = float(z)
    trace = {
        "lat": lat,
        "lng": lng
    }
    userInit = db.child("cova")
    results = userInit.child(x).set(trace)
    return HttpResponse("ok")