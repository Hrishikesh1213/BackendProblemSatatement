from gs_django.settings import BASE_DIR
from django.shortcuts import render
from django.http import HttpResponse
from pprint import pprint
import os

#import sys, subprocess
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gspread'])

import gspread
from oauth2client import client
from oauth2client.service_account import ServiceAccountCredentials

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name' : 'Hrishikesh'})

def getAllLocations(request):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(BASE_DIR, 'locations/creds.json'), scope)

    client = gspread.authorize(creds)

    sheet = client.open("TestSheet47").worksheet('Locations')

    data = sheet.get_all_records()

    return render(request, 'locations.html', {'data' : data})

def getLocation(request):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name(os.path.join(BASE_DIR, 'locations/creds.json'), scope)

    client = gspread.authorize(creds)

    sheet = client.open("TestSheet47").worksheet('Locations')

    data = sheet.get_all_records()

    val1 = request.GET['q']

    specfic = []

    for obj in data:
        if obj["Locations"][0] == val1:
            specfic.append(obj)

    return render(request, 'locations.html', {'data' : specfic})
