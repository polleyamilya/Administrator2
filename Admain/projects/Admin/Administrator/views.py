from django.shortcuts import render,redirect
from Administrator.forms import AdministratorForm
from Administrator.models import Administrator
def adm(request):
    if request.method == "POST":
        form = AdministratorForm(requests.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/view')
            except:
                pass
else:
    form =AdministratorForm()
return render(request,'index.html',{'form':form})                        

def view(request):
    Administrator =Administrator.objects.all()
   
    return render(request,"view.html",{'Administrator':Administrator})

def delete(requests, sId):
    Administrator = Administrator.objects.get(sId=sId)
    Administrator.delete()
    return redirect("/view")    

def edit(requests, sId):
    Administrator = Administrator.objects.get(sId=sId)
    
    return render(request,'edit.html',{'Administrator':Administrator})    