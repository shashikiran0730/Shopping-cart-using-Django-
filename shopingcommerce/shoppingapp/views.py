from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.shortcuts import render
from django.http import HttpResponse
from django.http import request
from django.core.mail import send_mail
from django.conf import settings 
from .models import orderconform, product
from .carts import cart
from shoppingapp.models import product
from shoppingapp.models import mycart,adminlogin as al
from . import sample
object=sample.login()

from os import X_OK, name
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
cred1 = credentials.Certificate({
  "type": "service_account",
  "project_id": "shoppingpython",
  "private_key_id": "df2573d57b6c24ea9865bf986a46aa624e86eaa6",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCU1rOVIOqBACzQ\nesHIDtDrru3t0wbmmuKidmj0G+C2ndOJZZvQa0pNahMjKBbOCf8v+JReK4WCb3Mw\naR55/AcaFuMGS8BOGdBF0A30jaZsrL6Tcdr1NSQ50/Iw+Y17cx8qeVKal7LmnkDL\nXj3dElS/hAgW91QgWARBnBSqdJAe5kBS6ogadwj0EZu2wGqi2YugzKv4elCN45xk\nVbmQdigSb4IQBgEAZdVO2RgUh73621D8yyz6kk12AlGSA9OHOQ5Ek4q52Bn6QX+t\nad5Mk19igAFRc8/rVPRDlF/6KOEKX14z5FtO3X9ZUvvg4209POHtbie4I8LKFbfF\nKJI8Tt89AgMBAAECggEAEa8Criy3f/Uv3eM/48+S1fW2MiP49WwgkjHkXWB0je3p\nhLEMVrJwpQr91Bb+wqMgbSgpJJkiJzGrq2xJ4S9m/pwKhCR66Cyb+Ldz+QLda5sI\nl4cW/zw9nhtG8rerrieq48Z/YHu2lzzlMOR1EC+N3yVGOshO9/rNIqhzMh9gQjNl\nrWjXS0Q8ciq3+hYAinGnsSFk+EbBP/EyjiiPZ3JRGdGxDBbx0e8ia2KUpL0Ig9HU\n/sx/VaGdOO+6kJgSmPyXLxQ37bnA/OoG/h7wscc8dyc57lxbmJNSv9fViUSKN474\n1dK1zqKVpQOo29V1jEwic8tHZUA1ebGOuglCOkWYgQKBgQDNs6G8UGUDvzauMMag\nWXruNK0f4rftEdX9d56rndtrDAYEz/18xe7JdwzZ+krwuWOvd1wtHB1th3Q/6rZu\nhW8E7IM5s/f8QyTrDvH0TMFzLoS0p9EM2Zfg8V+QCHxNEwj0FpQvSbWVlMIV7tw5\ndc1nrDgZQwlN3cODz0V24sRMwQKBgQC5O5l0P+sixDY1DflPLcuhySFvMlKJ7aFF\n+sQv3Eo0Hnf+GppD278muDgUXt0BTjZb4e83jyABqZRqDN9hY3Y58pt0Fqt46WWr\ni9AMTLj6JY7/nI65gRBs7EzM4hJAfLcLc2J/MEttkfUpfgayUNcylZVco5J34qM7\nY0Eccz2lfQKBgEbUzyGQMWh75HFQ3GSEy17RBrhPEnRwytXv5dRElDSlPEFV+XyI\nj7QR6Xv5wupnfBsEp9nkr4FyviXwRYeDLPpuErXA8eiMml7Sk6BC+e4Wm521l7es\nCa9sjjKDqYHExzV9vOMXp45tXfO9f1nN5cAIPnz8Z2zHqzZtHgdVCLFBAoGAb+Nb\nX0gY3YhOAiAtvzE3dsOKaaOpDd23dBD0nsBfJjpdWuVw15qOTXIrlcpzjw1Sco/4\nMsRGnhp0Jtcdu7MbwAcW9bmX3FKHcmbixfs2JQu45BgKcm1Ooaze+0d3pPJwkv8g\nuRlQBqCKyYRxwRZp1wlaDnpTyAzjcsUSmH/X9fUCgYEAurVqI2oieAtijueFf6Lg\nciINrqZYqSHvT2ep+O4rby7LiY56y2sKJhy19tAULeeIZj4b1HZh4bAJOjJlHXLY\n0JUseVaCAINy6fHRE3FEPtickptEC1yHXJzIYwjKKM1Nt0D3EWiCed98blIikqIh\nafHYBXUnOP+MNMDeWQRzvYs=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-iax8m@shoppingpython.iam.gserviceaccount.com",
  "client_id": "109314577559904457432",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "cgilient_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-iax8m%40shoppingpython.iam.gserviceaccount.com"
}
)

firebase_admin.initialize_app(cred1)
db=firestore.client()
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        data=({'name':name,'email':email,'mobile':mobile,'password':password})
        db.collection('shoppingRegister').document(email).set(data)
        return redirect('/login')
    return render(request,'register.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        request.session['customername']=email
        request.session.modified=True
        object.loginverify(email)
        password=request.POST['password']
        docs=db.collection('shoppingRegister').where('email','==',email).get()
        for i in docs:
            if i.to_dict()['email']==email:
                if i.to_dict()['password']==password:
                    return redirect('/afterlogin')
                return render(request,'login.html')
            return render(request,'login.html')
    return render(request,'login.html')

def afterlogin(request):
    name=request.session['customername']
    p=product.objects.all()
    return render(request,'afterlogin.html',{'products':p,'name':name})

def addtocart(request):
    id=request.POST['id']
    quantity=request.POST['quantity']
    p=product.objects.get(Itemid=id)
    event=mycart.objects.filter(Itemid=id)
    price=int(p.price)*int(quantity)
    en=mycart(customeremail=request.session['customername'],Itemid=p.Itemid,Itemname=p.Itemname,category=p.category,imageurl=p.imageurl,description=p.description,price=price,quantity=quantity)
    en.save()
    return redirect('/afterlogin')   

def viewmycart(request):
    n=request.session['customername']
    if request.method=="POST":
        g=request.POST['id']
        try:
            event=mycart.objects.get(id=g)
            event.delete()
            event=mycart.objects.all()
            if event!=None:
                for i in event:
                    price=i.price*i.quantity
                    return render(request,'mycart.html',{'products':event,'price':price})
            return render(request,'mycart.html',{'cart':'your cart is empty'})  
        except:
            event=mycart.objects.all()
            for i in event:
                price=i.price*i.quantity
            if event!=None:
                return render(request,'mycart.html',{'products':event,'price':price})
            else:
                return render(request,'mycart.html',{'cart':'your cart is empty'})
            
    else:
            p=mycart.objects.filter(customeremail=n)
            if len(p)==0:
                return render(request,'mycart.html',{'cart':'your cart is empty'})
            return render(request,'mycart.html',{'products':p})
def buynow(request):
    p=mycart.objects.filter(customeremail=request.session['customername'])
    s=0
    for i in p:
        s+=i.price
    request.session['bill']=str(s)
    return render(request,'buynow.html',{'products':p,'bill':s})

def payment(request):
    n=(request.session['bill'])
    event=orderconform.objects.filter(customeremail=request.session['customername'])
    event.delete()
    event=mycart.objects.all()
    for i in event:
        price=i.price*i.quantity
        d=orderconform(customeremail=request.session['customername'],Itemid=i.Itemid,Itemname=i.Itemname,price=price,quantity=i.quantity,totalprice=n)
        d.save()
    return render(request,'enjoyshopping.html')

def adminlog(request):
    if request.method=='POST':
        empid=request.POST['empid']
        securitycode=request.POST['code']
        password=request.POST['password']   
        p=al.objects.all()
        for i in p:
            if str(i.empid)==str(empid):
                if str(i.securitycode)==str(securitycode):
                    if str(i.password)==str(password):
                        return redirect('/afteradminlogin')
                    else:
                        status="incorrect password"
                        return render(request,'adminlog.html',{'status':status})
                else:
                    status="incorrect security code"
                    return render(request,'adminlog.html',{'status':status})
            else:
                status="incorrect empid"
                return render(request,'adminlog.html',{'status':status})
    return render(request,'adminlog.html')
def afteradminlogin(request):
    products=orderconform.objects.all()
    return render(request,'afteradminlogin.html',{'products':products})
def updatestatus(request):
    if request.method=="POST":
        g=request.POST['status']
        id=request.POST['shashiid']
        print(id)
        products=orderconform.objects.all()
        for i in products:
            if str(i.id)==str(id):
                i.status=g
            i.save()
        return render(request,'afteradminlogin.html',{'products':products})
    return render(request,'afteradminlogin.html')



