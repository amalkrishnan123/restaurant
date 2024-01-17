from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home2.html')
def foodmenu(request):
    return render(request,'foodmenu.html')
def story(request):
    return render(request,'story.html')
def contact(request):
    return render(request,'contact.html')
def soup(request):
    return render(request,'soup.html')
