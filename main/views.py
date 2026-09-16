from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import EducationForm
from main.models import Experience
from main.models import Education


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

def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education = [edu.object for edu in education]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "title_query": title_query,
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Riwayat pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    title_query = request.GET.get("institution", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(institution__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Education berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")