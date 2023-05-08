from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Create your views here.
def diabetic(request):
    pregnancies = float(request.POST['pregnancy'])
    glucose = float(request.POST['glucose'])
    bloodpressure = float(request.POST['bloodPressure'])
    skinthickness = float(request.POST['skinThickness'])
    insulin = float(request.POST['insulin'])
    bmi = float(request.POST['BMI'])
    diabetesfun = float(request.POST['diabetesPedigreeFunction'])
    age = float(request.POST['age'])
    testData = [[pregnancies,glucose,bloodpressure,skinthickness,insulin,bmi,diabetesfun,age]]
    model = joblib.load("model/diabetics.pkl")
    isDiabetic = model.predict(testData)
    data = {'isDiabetic':isDiabetic[0]}
    result1 = ""
    if isDiabetic == 1:
        result1 = "Oops! You have DIABETES ????."
    else:
        result1 = "Great! You DON'T have diabetes ????."
    return render(request,'home/home.html',{'result':result1})

def homePage(request):
    return render(request,'home/home.html')

def code(request):
    return render(request,"code/Dibetics_Pred.html")

