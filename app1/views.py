from django.shortcuts import render

# Create your views here.
def vamsi(request):
    r={'poojitha':'vamsi'}
    return render(request,'h1.html',r)