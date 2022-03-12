from django.shortcuts import render

global x
x='l'
class login():
    def loginverify(request,x1):
        global x
        x=x1
        if x=='s':
            return render(request,'login.html')
