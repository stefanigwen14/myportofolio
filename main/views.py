from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "npm": "2506594263",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Hello, my name's Gwen and I'm currently a 2nd Year Information Systems student at Universitas Indonesia. Welcome to my portfolio website where I showcase my stuff! :D"
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)