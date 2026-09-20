from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import ProjectForm, TestimonialForm
from main.models import Experience, Project, Testimonial
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
    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "education_list": Education.objects.all(),
    }
    return render(request, "education.html", context)

def create_project(request):
    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New project has been successfully added! ( ˶ˆᗜˆ˵ )")
        return redirect("main:show_projects")

    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "form": form,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "project_list": Project.objects.all(),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    projects_json = serializers.serialize("json", projects)
    return HttpResponse(projects_json, content_type="application/json")

def show_projects(request):
    json_response = get_projects_json(request)

    projects = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    projects = [project.object for project in projects]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "project_list": projects,
        "title_query": title_query,
    }
    return render(request, "project.html", context)

def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project successfully deleted!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

def create_testimonial(request):
    form = TestimonialForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "New testimonial has been successfully added! ( ˶ˆᗜˆ˵ )")
        return redirect("main:show_testimonials")

    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "form": form,
    }
    return render(request, "testimonials_form.html", context)

def show_testimonials(request):
    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "testimonial_list": Testimonial.objects.all(),
    }
    return render(request, "testimonial.html", context)

def get_testimonials_json(request):
    category_query = request.GET.getlist("testimonial_category")
    testimonials = Testimonial.objects.all()
    categories = []

    if category_query:
        # checking which categories are in the query
        if "Education" in category_query:
            categories.extend(list(Education.objects.values_list("institution", flat=True)))
        if "Experience" in category_query:
            categories.extend(list(Experience.objects.values_list("title", flat=True)))
        if "Projects" in category_query:
            categories.extend(list(Project.objects.values_list("title", flat=True)))
        if "Others" in category_query:
            categories.extend(["Others", "others"])
        # filtered if the relevant_experience is in the categories that are in the query
        testimonials = testimonials.filter(related_experience__in=categories)

    testimonials_json = serializers.serialize("json", testimonials)
    return HttpResponse(testimonials_json, content_type="application/json")

def show_testimonials(request):
    json_response = get_testimonials_json(request)

    testimonials = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    testimonials = [testimonial.object for testimonial in testimonials]
    category_query = request.GET.getlist("testimonial_category")

    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "testimonial_list": testimonials,
        "category_query": category_query,
    }
    return render(request, "testimonial.html", context)

def delete_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if request.method == "POST":
        testimonial.delete()
        messages.success(request, "Testimonial successfully deleted!")
        return redirect("main:show_testimonials")

    return redirect("main:show_testimonials")

def edit_testimonial(request, testimonial_id):
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)

    if request.method == "POST":
        form = TestimonialForm(request.POST, instance=testimonial)
        if form.is_valid():
            form.save()
            messages.success(request, "Testimonial has been successfully edited! ( ˶ˆᗜˆ˵ )")
            return redirect("main:show_testimonials")
    else:
        form = TestimonialForm(instance=testimonial)

    context = {
        "name": "Stefani Gwen Rolanda Tumbelaka",
        "nickname": "Gwen",
        "form": form,
        "testimonial": testimonial,
    }
    return render(request, "testimonial_edit_form.html", context)

        