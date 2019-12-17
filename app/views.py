from django.shortcuts import redirect #"go to the post_detail page for the newly created post"

from django.shortcuts import render, get_object_or_404
from app.models import Sslc, Puc, Engineering, Masters 
from django.http import HttpResponse
from django.utils import timezone
from app import forms
from django.contrib.auth.decorators import login_required

from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail

# Create your views here.
@login_required    
def homepage(request):
    # ctg1=Sslc.objects.all()
    user_name=request.session.get('username',"No User")
    c1=Sslc.objects.all().count()
    c2=Puc.objects.all().count()
    c3=Engineering.objects.all().count()
    c4=Masters.objects.all().count()
    context = {
        'ctg1': 'SSLC',
        'ctg2': 'PUC',
        'ctg3': 'Engineering',
        'ctg4': 'Masters',
        'c1':c1,
        'c2':c2,
        'c3':c3,
        'c4':c4,
        'user_name':user_name
    }
    return render(request,'homepage.html',context)



# List view
def post_list_sslc(request):
    sslc = Sslc.objects.all()
    return render(request, 'listview/sslc.html', {'sslc': sslc})

def post_list_puc(request):
    puc = Puc.objects.all()
    return render(request, 'listview/puc.html', {'puc': puc})

def post_list_engg(request):
    engg = Engineering.objects.all()
    return render(request, 'listview/engg.html', {'engg': engg})

def post_list_masters(request):
    mstr= Masters.objects.all()
    return render(request, 'listview/masters.html', {'masters': mstr})

# Detail view
def post_detail_sslc(request, pk):
    post = get_object_or_404(Sslc, pk=pk)
    return render(request, 'detailview/sslc_detail.html', {'post': post})

def post_detail_puc(request, pk):
    pu = get_object_or_404(Puc, pk=pk)
    return render(request, 'detailview/puc_detail.html', {'pu': pu})

def post_detail_engg(request, pk):
    en = get_object_or_404(Engineering, pk=pk)
    return render(request, 'detailview/engg_detail.html', {'en': en})

def post_detail_masters(request, pk):
    post = get_object_or_404(Masters, pk=pk)
    return render(request, 'detailview/masters_detail.html', {'post': post})

class CreateSslcView(CreateView):
    model=Sslc
    fields=('category','book_title','auth_name','published_date','text')
# ###########################################################################################

def register(request):
    register=False
    if request.method=="POST":
        user_form=forms.User_Form(request.POST)
        user_data_form=forms.User_data_form(request.POST,request.FILES)
        if user_form.is_valid() and user_data_form.is_valid():
            user=user_form.save(commit=True)
            user.set_password(user.password)
            user.save()

            user_data=user_data_form.save(commit=False)
            user_data.user=user

            if 'profile_pic' in request.FILES:
                user_data.profile_pic=request.FILES['profile_pic']
            user_data.save()
            register=True
            send_mail("Registration Successful","Thank You For Registering","noreply2user.infotech@gmail.com", \
                [user.email],fail_silently=False) 
     #here we give user.email.............so it will also send to the unknow person who is going to signup here
    else:
        user_form=forms.User_Form()
        user_data_form=forms.User_data_form()
    
    d={'form':user_data_form,'form_user':user_form,'register':register}
    return render(request,'app/register.html',context=d)

def index(request):
    user_name=request.session.get('username',"No User")
    return render(request,'app/base.html',context={'user_name':user_name})


def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username',"")
        password=request.POST.get('password','')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                # request.session['username']=username
                request.session['username']=(username) #,user.email
# here we want to display both username&profile_pic after login...username & email are working
# profilepic need to check and need to give the path
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("Not an Active user")
        else:
            print("Invalid Login")
            return render(request,'app/login.html')
            # return HttpResponse("Invalid Login")
    else:
        return render(request,'app/login.html')
        # return render(request,'homepage.html')


@login_required
def user_logout(request):
    logout(request)
    try:
        del request.session['username']
    except:
        pass
    return HttpResponseRedirect(reverse('index'))
    

@login_required
def wish(request):
    # return HttpResponse("<h1>Hai Mr./Ms. {} </h1>".format(request.session['username']))
    return HttpResponse("<h1>Hai Mr./Ms. {} </h1>")
