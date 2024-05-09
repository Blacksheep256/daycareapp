from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import F, Count
from django.db.models.functions import Length


# Create your views here.

def dollssales_reg(request):
    submitted = False
    if request.method == "POST":
        form = DollssalesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/dollsales?submitted=True")
    else:
        form = DollssalesForm
        if "submitted" in request.GET:
            submitted = True
    
    form = DollssalesForm
    return render(
        request,
        "daycareapp/dollssalesform.html",
        {'form': form, 'submitted': submitted})



def schoolfees(request):
    instance = Schoolfees.objects.all()

    # form = SchoolfeesForm()
    form = SchoolfeesForm()
    if request.method == "POST":
        form = SchoolfeesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin-panel')
        else:
            form = SchoolfeesForm()
    context = {'instance':instance, 'form':form}
    return render(request, 'daycareapp/schoolfeesform.html', context)



def dollsdashboard(request):

    dolls = Dollsdashboard.objects.all()

    return render(request, "daycareapp/DollsDashboard.html",{"dolls":dolls})



def procure_form(request):
    submitted = False
    if request.method == "POST":
        form = ProcureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/procrueform?submitted=True")
    else:
        form = ProcureForm
        if "submitted" in request.GET:
            submitted = True
    
    form = ProcureForm
    return render(
        request,
        "daycareapp/procrueform.html",
        {'form': form, 'submitted': submitted})


def pro(request):
    procure = Procure.objects.all()
    if request.method == "POST":

        search = request.POST['search']
        procure = Procure.objects.filter(item__contains=search)
        return render(request, "daycareapp/procruelist.html", {"procure": procure, "search": search})


    else:


     return render(request, "daycareapp/procruelist.html", {"procure": procure})
      
    



def babysitter_delete(request, babysitter_id):
   
   delete2 = Babysitter.objects.get(pk=babysitter_id)
   delete2.delete()
   return redirect('list-babysitter')

def baby_delete(request, baby_id):

    delete1 = Baby.objects.get(pk=baby_id)
    delete1.delete()
    return redirect('list-babies')

def baby_update(request, baby_id):
       
       update2 = Baby.objects.get(pk=baby_id)
       form = BabyregForm(request.POST or None, instance=update2)
       if form.is_valid():
            form.save()
            return redirect('list-babies')
 
       return render(request, "daycareapp/updateprofile2.html", {"update2": update2,"form":form})

def babysitter_update(request, babysitter_id):
       update1 = Babysitter.objects.get(pk=babysitter_id)
       form = BabysiiterregForm(request.POST or None, instance=update1)
       if form.is_valid():
            form.save()
            return redirect('list-babysitter')
 
       return render(request, "daycareapp/updateprofile1.html", {"update1": update1,"form":form})



def home(request):
    return render(request, "daycareapp/login1.html")


def list_babies(request):
    babies = Baby.objects.all()

    if request.method == "POST":

        searched = request.POST['searched']
        babies = Baby.objects.filter(first_name__contains=searched)

    
        return render(request, "daycareapp/babies-list.html", {"babies": babies,"searched":searched,})
    
    else:

       return render(request, "daycareapp/babies-list.html", {"babies": babies})


def list_babysitter(request):
    siter = Babysitter.objects.all()
    if request.method == "POST":

        search = request.POST['search']
        siter = Babysitter.objects.filter(first_name__contains=search)

        return render(request, "daycareapp/babysitter list.html", {"siter": siter,"search":search,})

    else:

       return render(request, "daycareapp/babysitter list.html", {"siter": siter})


def child_profile(request, pk,):  
    child1 = Schoolfees.objects.all

  

  
    return render(request, "daycareapp/child profile.html", {"child1": child1, })


def child_reg(request):
    submitted = False
    if request.method == "POST":
        form = BabyregForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/child-reg?submitted=True")
    else:
        form = BabysiiterregForm
        if "submitted" in request.GET:
            submitted = True
    
    form = BabyregForm
    return render(
        request,
        "daycareapp/child reg.html",
        {'form': form, 'submitted': submitted})

def babysitter_reg(request):
    submitted = False
    if request.method == "POST":
        form = BabysiiterregForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/babysitter-reg?submitted=True")
    else:
        form = BabysiiterregForm
        if "submitted" in request.GET:
            submitted = True

    form = BabysiiterregForm
    return render(
        request,
        "daycareapp/baby sitter reg.html",
        {'form': form, 'submitted': submitted})


def babysitter_profile(request, pk):
    babysitter = Babysitter.objects.get(id=pk)
    return render(
        request, "daycareapp/babysitter profile.html", {"babysitter": babysitter}
    )


def admin_panel(request):
    return render(request, "daycareapp/Admin panel.html")
