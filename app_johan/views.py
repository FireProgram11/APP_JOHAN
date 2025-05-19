from django.shortcuts import render

def show_form(request):
    return render(request, 'app_johan/form.html')