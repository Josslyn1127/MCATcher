from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
# this is how you load the model you've made in sklearn
import joblib

# our model is expecting a dataframe so we have to create one
reloadModel = joblib.load("./models/RFModelforMPG.pkl")

def index_view(request, *args, **kwargs):
    context = {'a': 'Helloworld!'}
    return render(request, "index.html", context)

def index(request):
    return render(request, "firstpage/index.html")

def predictMPG_view(request):
    print(request)
    if request.method == 'POST':
        temp={}
        temp['cylinders']=request.POST.get('cylinderVal')
        temp['displacement']=request.POST.get('dispVal')
        temp['horsepower']=request.POST.get('hrsPwrVal')
        temp['weight']=request.POST.get('weightVal')
        temp['acceleration']=request.POST.get('accVal')
        temp['model_year']=request.POST.get('modelVal')
        temp['origin']=request.POST.get('originVal')

    testDtaa=pd.DataFrame({'x':temp}).transpose()
    scoreval = reloadModel.predict(testDtaa)[0]
    context = {'scoreval': scoreval}
    return render(request, "index.html", context)
