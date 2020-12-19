from django.shortcuts import render,HttpResponseRedirect
from .forms import RegForm,UserDetailForm,loginform
from .models import UserDetail
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def CreateAcc(request):
    if request.method == 'POST':
        frm = RegForm(request.POST)
        ufrm = UserDetailForm(request.POST,request.FILES)
        if frm.is_valid() & ufrm.is_valid():
            UserID = -1
            UserName = frm.cleaned_data['username']
            frm.save()
            Enroll = ufrm.cleaned_data['enroll_no']
            Roll = ufrm.cleaned_data['roll_no']
            Mobile = ufrm.cleaned_data['mobile']
            pic = ufrm.cleaned_data['photo']
            UserData = UserDetail(user_id=UserID,username=UserName,enroll_no=Enroll,roll_no=Roll,mobile=Mobile,photo=pic)
            UserData.save()
            messages.success(request,'Admit Card Generated ')
            return HttpResponseRedirect('/login')
    else:
        frm = RegForm()
        ufrm = UserDetailForm()
    return render(request,'CreateAccount.html',{'form':frm,'uform':ufrm})

def loginPage(request):
    if request.method == 'POST':
        frm = loginform(request=request,data=request.POST)
        if frm.is_valid():
            UserName = frm.cleaned_data['username']
            Password = frm.cleaned_data['password']
            verify = authenticate(username=UserName,password=Password)
            if verify is not None:
                login(request,verify)
                return HttpResponseRedirect('/AdmitCard')
    else:
        frm = loginform()
    return render(request,'login.html',{'form':frm})

def AdmitCardPage(request):
    UserName = request.user.username
    data = UserDetail.objects.get(username=UserName)
    return render(request,'admitcard.html',{'data':data})

def Logoutpage(request):
    logout(request)
    return HttpResponseRedirect('/login')