from django.shortcuts import render

# Create your views here.
def app(request):
    d={'NAME':'HAZEERA','AGE':'25'}
    return render(request,'app.html',context=d)