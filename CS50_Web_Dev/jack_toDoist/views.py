from django.shortcuts import render

tasks = ["lundary", "shopping", "study"]
# Create your views here.
def index(request):
    # A very often seeing pattern in django
    # Create a variable and implement logic in the web pages
    return render(request, "index.html", {
        "tasks": tasks
    })

def add(request):
    return render(request, "add.html")