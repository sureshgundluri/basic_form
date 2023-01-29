from django.shortcuts import render
from django.http import HttpResponse

def html_form(request):
    # if request.method=='POST':
    #     un=request.POST['usn']
    #     pw=request.POST['psw']
    #     print(un)
    #     print(pw)
    #     return HttpResponse('Data submited')
    return render(request,'html_form.html')


