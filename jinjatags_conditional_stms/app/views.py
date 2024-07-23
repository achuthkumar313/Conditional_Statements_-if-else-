from django.shortcuts import render

# Create your views here.
def conditional(request):
    context={'a':215,'b':50,'c':325,'d':100}
    return render(request,'conditional.html',context)