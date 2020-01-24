from django.shortcuts import render

def allaboutmodels(request):
    template_name = 'allaboutmodels/home.html'
    context = locals()
    return render(request,template_name,context)

