from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponseRedirect
from .models import Emp
from django.http import HttpResponse

# Create your views here.
# def user(request):
#     return HttpResponse("Hello world")


def user(request):
    if request.method == 'POST':
        empname = request.POST['name']
        empemail = request.POST['email']
        empmsg = request.POST['message']
        empGender = request.POST['Gender']
        data = Emp(Emp_name=empname, Emp_email=empemail, Emp_message=empmsg, Emp_Gender=empGender)
        data.save()
        # a = Emp.objects.all()
        # return render(request, "index.html", {"data": a})
    return render(request, "index.html")


def details(request):
    if request.method == "GET":
        a = Emp.objects.all()
        return render(request, "data.html", {"data": a})
    elif request.method == "POST":
        return HttpResponseRedirect(request.path)


def update(request):
    if request.method == 'POST':
        id = request.POST["id"]
        empname = request.POST['name']
        empemail = request.POST['email']
        empmsg = request.POST['message']
        empGender = request.POST['Gender']
        # use get_object_or_404 to get the object by ID or return a 404 response if not found
        x = get_object_or_404(Emp,pk=id)
        # update the fields
        x.Emp_name = empname
        x.Emp_email = empemail
        x.Emp_message = empmsg
        x.Emp_Gender = empGender
        # save the updated objects
        x.save()
        # Redirect to the details page after the update
        return HttpResponseRedirect ("/data/")
    return HttpResponse ("method not allowed", status=405)
    
        
def Delete(request,id):
    if request.method == 'POST':
        a=Emp.objects.get(pk=id)
        a.delete()
        return redirect('/data/')
    






















 



























     












        
    

























