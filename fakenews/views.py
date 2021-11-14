from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

import re
import string
import pandas as pd
import joblib
import math
import numpy as np

Model = joblib.load(r"C:\Users\iiit\Downloads\mini_project2\fake_news_detection\fakenews/Model.pkl")

def index(request):
    return render(request, "fakenews/fakeNewsDetection.html")

# Create your views here.

def wordpre(text):
    text = text.lower()
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub("\\W"," ",text) # remove special chars
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub(r'\w*\d\w*', '', text)
    return text

def detect(request):
    flag=0
    if request.method == 'POST':
        txt= request.POST["txt"]
        if len(txt) == 0:
              flag=1
        txt = wordpre(txt)
        txt = pd.Series(txt)
        result = Model.predict(txt)
        prob=Model.predict_proba(txt)
        p=prob[0][result]*100
        probability=math.ceil(p[0])
        return render(request, "fakenews/fakeNewsDetection.html", {
        "result":result,
        "probability" : probability,
         "flag":flag
         })
    return '' 