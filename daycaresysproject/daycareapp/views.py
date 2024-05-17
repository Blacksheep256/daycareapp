from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.db.models import F, Count
from django.db.models.functions import Length
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
# Logout view
# def logout_view(request):
#     logout(request)
#     return redirect('login')

def restricted_page(request):
    return render(request, 'restricted_page.html')

# Login view
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('restricted_page')
#         else:
#             return HttpResponse("Invalid login details")
#     return render(request, 'daycareapp/login.html')





@login_required
def schoolfeeslist(request):
    fees = Schoolfees.objects.all()

    if request.method == 'GET':
        form = SchoolFeesSearchForm(request.GET)
        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            first_name = form.cleaned_data.get('first_name')

            # Start with all records
            results = Schoolfees.objects.all()

            # Filter by date range if both dates are provided
            if start_date and end_date:
                results = results.filter(date_of_payment__date__range=(start_date, end_date))

            # Filter by first name if provided
            if first_name:
                results = results.filter(baby__first_name__icontains=first_name)
        
    else:
        form = SchoolFeesSearchForm()
        results = Schoolfees.objects.none()

    return render(request, 'daycareapp/schoolfeeslist.html', {'form': form, 'results': results,'fees':fees})

@login_required
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



@login_required
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




@login_required
def dollsdashboard(request):

    sales = Dollsdashboard.objects.all()
    total_dolls_sold= sum(sale.dollsbought for sale in sales)
    return render(request, 'daycareapp/DollsDashboard.html', {'sales': sales, 'total_dolls_sold': total_dolls_sold})




@login_required
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

@login_required
def pro(request):
    procure = Procure.objects.all()
    if request.method == "POST":

        search = request.POST['search']
        procure = Procure.objects.filter(item__contains=search)
        return render(request, "daycareapp/procruelist.html", {"procure": procure, "search": search})


    else:


     return render(request, "daycareapp/procruelist.html", {"procure": procure})
      
    



@login_required
def babysitter_delete(request, babysitter_id):
   
   delete2 = Babysitter.objects.get(pk=babysitter_id)
   delete2.delete()
   return redirect('list-babysitter')

def baby_delete(request, baby_id):

    delete1 = Baby.objects.get(pk=baby_id)
    delete1.delete()
    return redirect('list-babies')

@login_required
def baby_update(request, baby_id):
       
       update2 = Baby.objects.get(pk=baby_id)
       form = BabyregForm(request.POST or None, instance=update2)
       if form.is_valid():
            form.save()
            return redirect('list-babies')
 
       return render(request, "daycareapp/updateprofile2.html", {"update2": update2,"form":form})

@login_required
def babysitter_update(request, babysitter_id):
       update1 = Babysitter.objects.get(pk=babysitter_id)
       form = BabysiiterregForm(request.POST or None, instance=update1)
       if form.is_valid():
            form.save()
            return redirect('list-babysitter')
       
       return render(request, "daycareapp/updateprofile1.html", {"update1": update1,"form":form})


@login_required
def list_babies(request):
    babies = Baby.objects.all()

    if request.method == "POST":

        searched = request.POST['searched']
        babies = Baby.objects.filter(first_name__contains=searched)

    
        return render(request, "daycareapp/babies-list.html", {"babies": babies,"searched":searched,})
    
    else:

       return render(request, "daycareapp/babies-list.html", {"babies": babies})


@login_required
def list_babysitter(request):
    siter = Babysitter.objects.all()
    if request.method == "POST":

        search = request.POST['search']
        siter = Babysitter.objects.filter(first_name__contains=search)

        return render(request, "daycareapp/babysitter list.html", {"siter": siter,"search":search,})

    else:

       return render(request, "daycareapp/babysitter list.html", {"siter": siter})


@login_required
def child_profile(request, pk): 
    

    #child1 = Schoolfees.objects.get(id=pk)
    child = Baby.objects.get(id=pk)
    return render(
        request, "daycareapp/child profile.html", {"child": child,})

 




@login_required
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


@login_required
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


@login_required
def babysitter_profile(request, pk):
    babysitter = Babysitter.objects.get(id=pk)
    return render(
        request, "daycareapp/babysitter profile.html", {"babysitter": babysitter}
    )


@login_required
def admin_panel(request):
    return render(request, "daycareapp/Admin panel.html")