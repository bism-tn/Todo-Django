from django.shortcuts import render,redirect

from  taskmanager.models import User,Taskmodel

from django.db.models import Sum


from django.contrib.auth import login,logout

from django.contrib.auth import authenticate

from django.views.generic import View

from taskmanager.forms import Userform

from taskmanager.forms import LoginForm,TaskForm,TaskUpdateForm
from django.utils.decorators import method_decorator


def is_user(fn):
    def wrapper(request,**kwargs):
        id = kwargs.get("pk")
        data =  Taskmodel.objects.get(id = id)
        if data.user == request.user:
            return fn(request,**kwargs) 
        else:
            return redirect("login")
    return wrapper

# Create your views here.
#view:userregistration
#methods:get/post
#url:localhost:8000/taskmaager/signup


class UserresgisterView(View):

    def get(self,request):

        form = Userform

        return render(request,"signup.html",{"form":form})
    
    def post(self,request):

        form=Userform

        data=Userform(request.POST)

        if data.is_valid():

            print(data.cleaned_data)
            User.objects.create_user(**data.cleaned_data)

        return render(request,'signup.html',{'form':form})
    


class LoginView(View):

    def get(self,request):
        form =LoginForm

        return render(request,"login.html",{"form":form})

    def post(self,request):
        form=LoginForm

        form=LoginForm(request.POST)

        u_name =request.POST.get("username")
        pwd =  request.POST.get("password")
        user_obj = authenticate(request,username=u_name,password=pwd)
        if user_obj:
            login(request,user_obj)
            print("logedin")
            return redirect("all_task")
        else:

            form=LoginForm

            print("not logged in")

            return render(request,"login.html",{"form":form})

class TaskAddView(View):

    def get(self,request):
        
        form = TaskForm

        return render(request,'add.html',{'form':form})
    
    def post(self,request):

         

         data=TaskForm(request.POST)

         if data.is_valid():
             
             
             
             Taskmodel.objects.create(**data.cleaned_data,user=request.user)

         form = TaskForm
         return redirect("all_task")
    

class TaskreadView(View):
     def get(self,request):
        # data=Taskmodel.objects.all()
        data=Taskmodel.objects.filter(user=request.user).order_by('status')
        return render(request,"alltask.html",{"data":data})


class TaskdeleteView(View):
    def get(self,request,**kwargs):

        id = kwargs.get("pk")

        data = Taskmodel.objects.get(id=id)
        if data.user == request.user:

            data.delete()

            return redirect("all_task")
        else:
            return redirect("login")
       

@method_decorator(decorator=is_user,name="dispatch")
class TaskDetailView(View):
    def  get(self,request,**kwargs):
        id =kwargs.get("pk")

        data =Taskmodel.objects.get(id=id)
        return render(request,"details.html",{"data":data})
    

@method_decorator(decorator=is_user,name="dispatch")
class TaskupdateView(View):

    def get(self,request,**kwargs):

        id= kwargs.get("pk")

        data= Taskmodel.objects.get(id=id)

        form= TaskUpdateForm(instance=data)

        return render(request,"update.html",{"form":form})
    
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        data= Taskmodel.objects.get(id=id)

        form= TaskUpdateForm(request.POST,instance=data)

        if form.is_valid():
            print("done")
            form.save()
        return redirect("all_task")

class Signout(View):
    def get(self,request):
        logout(request)

        return redirect("login")
    

class TaskcompleteView(View):
    def get(self,request,**kwargs):
       id =  kwargs.get("pk")
       data =Taskmodel.objects.get(id = id)
       data.complete()
            
       return redirect("all_task")

class Userdetails(View):
    def get(self,request):
        total = Taskmodel.objects.filter(user= request.user).count() 
        completed = Taskmodel.objects.filter(user =  request.user,status= True).count()
        incomplete =  total-completed
        data = Taskmodel.objects.filter(user =  request.user).aggregate(Sum('point'))
        High=Taskmodel.objects.filter(user =  request.user ,priority ="High",status="False" )
        Medium=Taskmodel.objects.filter(user =  request.user ,priority ="Medium",status="False"  )
        Low=Taskmodel.objects.filter(user =  request.user ,priority ="Low",status="False"  )
        # sum = 0
        # for i in data:
        #     sum+= i.point
        total_points = data.get('point__sum')
        return render(request,"Home.html",{"total":total,"complete":completed,"incomplete":incomplete,"points":total_points,"High":High,"Medium":Medium,"Low":Low})



class HomeView(View):
    def get(self,request):
        return render(request,"Home.html")