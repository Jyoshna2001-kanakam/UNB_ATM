from django.shortcuts import render,redirect,HttpResponse
from . forms import AtmForm
from . models import ATM
from decimal import Decimal
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth import settings
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
     return render(request,'index.html')

def create(request):
     form=AtmForm()
     # print(form)
     if request.method=='POST':
          form=AtmForm(request.POST,request.FILES)
          if form.is_valid():
               name=request.POST.get('name')
               email=request.POST.get('email')
               account_no=request.POST.get('account_no')
               print(name,email)
               try:
                    send_mail(
                         "Thanks for Registration",    #subject
                         f" \nDear Customer ...\n Thank you for creating account in UNION BANK .\n Your Account number is {account_no}  we are excited to have you on board!,\n thank you \n regards\n Jyoshna ",#body
                         settings.EMAIL_HOST_USER,
                         [email],
                         fail_silently=False,
                    )
                    print('Mail sent')
               except Exception as e:
                    return HttpResponse(f"Error sending email:{e}")
               form.save()
               return redirect('pin')
             
     return render(request,'create.html',{'form':form})

def pin(request):
     if request.method=='POST':
          account_no=request.POST.get('account_no')
          pin=request.POST.get('pin')
          print(account_no,pin)
          account_no=ATM.objects.get(account_no=account_no)
          pin1=account_no.pin=int(pin)
          # print(pin1)
          email=account_no.email
          account_no.save()
          print(email)
          try:
               send_mail(
                         "Thanks for Registration",    #subject
                         f" \nDear Customer ...\n You have succesfully created pin {pin1} in UNION BANK .\n we are excited to have you on board!,\n thank you \n regards\n Jyoshna ",#body
                         settings.EMAIL_HOST_USER,
                         [email],
                         fail_silently=False,
                    )
               print('Mail sent')
               return redirect('index')
          except Exception as e:
                    return HttpResponse(f"Error sending email:{e}")
          
     return render(request,'pin.html')

def balance(request):
     amount=0
     if request.method=="POST":
          account_no = request.POST.get("account_no")
          pin= request.POST.get("pin")
          print(account_no,pin)
          account_no=ATM.objects.get(account_no=account_no)
          pin=ATM.objects.get(pin=pin)
          email=account_no.email

          if account_no==account_no and pin==pin:
               amount=account_no.amount
               print(amount)
               try:
                   send_mail(
                         "Thanks for Registration",    #subject
                         f" \nDear Customer ...\n You current balance amount is {amount} in UNION BANK .\n Have a great day..!,\n thank you \n regards\n Jyoshna ",#body
                         settings.EMAIL_HOST_USER,
                         [email],
                         fail_silently=False,
                    )
                   print('Mail sent')
                   return redirect('balance')
               except Exception as e:
                    return HttpResponse(f"Error sending email:{e}")

          else:
               print('Invalid credentials')
               # return HttpResponse(f"Invalid credentials")
          # print(amount1)
               
     return render(request,'balance.html',{'amount':amount})

def withdraw(request):
     amount=0
     data=0
     if request.method=='POST':
          account_no=request.POST.get('account_no')
          pin=request.POST.get('pin')
          amount=request.POST.get('amount')
          print(account_no,pin,amount)
          data=ATM.objects.get(account_no=account_no)
          data=ATM.objects.get(pin=pin)
          email=data.email
     
          data.account_no=account_no
          data.pin=int(pin)
          data.amount-=int(amount)
          data.save()
          print(data.amount)
          try:
                   send_mail(
                         "Thanks for Registration",    #subject
                         f" \nDear Customer ...\n You current balance amount is {amount} in UNION BANK .\n Have a great day..!,\n thank you \n regards\n Jyoshna ",#body
                         settings.EMAIL_HOST_USER,
                         [email],
                         fail_silently=False,
                    )
                   print('Mail sent')
                   return redirect('balance')
          except Exception as e:
                    return HttpResponse(f"Error sending email:{e}")
          

     return render(request,'withdraw.html',{'data':data})

def deposite(request):
     amount=0
     data=0
     if request.method=='POST':
          account_no=request.POST.get('account')
          pin=request.POST.get('pin')
          amount=request.POST.get('amount')
          print(account_no,pin,amount)
     

          data=ATM.objects.get(account_no=account_no)
          data=ATM.objects.get(pin=pin)
          data.amount+=int(amount)
          email=data.email
          data.save()
          print(data.amount)
        
          try:
                   send_mail(
                         "Thanks for Registration",    #subject
                         f" \nDear Customer ...\n You current balance amount is {amount} in UNION BANK .\n Have a great day..!,\n thank you \n regards\n Jyoshna ",#body
                         settings.EMAIL_HOST_USER,
                         [email],
                         fail_silently=False,
                    )
                   print('Mail sent')
                   return redirect('balance')
          except Exception as e:
                    return HttpResponse(f"Error sending email:{e}")
          

     return render(request,'deposite.html',{'data':data})

def transfer(request):
     amount=0
     account=0
     account1=0
     if request.method=='POST':
          account_from=request.POST.get('account')
          account_to=request.POST.get('account1')
          pin=request.POST.get('pin')
          amount=request.POST.get('amount')
          print(account_from,account_to,pin,amount)

          account=ATM.objects.get(account_no=account_from)
          account1=ATM.objects.get(account_no=account_to)
          # email=account.email
          print(account.name)

          if account.pin==int(pin):
               if account.amount>Decimal(amount):
                    account.amount-=Decimal(amount)
                    account1.amount+=Decimal(amount)

                    account.save()
                    account1.save()
                    print(account.amount,account1.amount)
                    # try:
                    #      send_mail(
                    #      "Thanks for Registration",    #subject
                    #      f" \nDear Customer ...\n {amount}   is transfer to {account_to}  in UNION BANK .\n Have a great day..!,\n thank you \n regards\n Jyoshna ",#body
                    #      settings.EMAIL_HOST_USER,
                    #      [email],
                    #      fail_silently=False,
                    # )
                    #      print('Mail sent')
                    #      return redirect('index')
                    # except Exception as e:
                    #      return HttpResponse(f"Error sending email:{e}")
               else:
                    print('Insuffisient balance')
          else:
               print('Invalid credentials')
               return redirect('index')

     return render(request,'transfer.html',{'account':account,'account1':account1})