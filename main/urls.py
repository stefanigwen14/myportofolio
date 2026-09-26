from django.urls import path

from main.views import create_project, create_testimonial, delete_project, delete_testimonial, edit_testimonial, get_projects_json, get_testimonials_json, login_user, logout_user, register, show_main, show_experience, show_education, show_projects, show_testimonials, toggle_star

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("projects/add/", create_project, name="create_project"),
    path("projects/", show_projects, name="show_projects"),
    path("api/projects/", get_projects_json, name="get_projects_json"),
    path("projects/<uuid:project_id>/delete/",delete_project,name="delete_project"),
    path("testimonials/add/", create_testimonial, name="create_testimonial"),
    path("testimonials/", show_testimonials, name="show_testimonials"),
    path("api/testimonials/", get_testimonials_json, name="get_testimonials_json"),
    path("testimonials/<uuid:testimonial_id>/delete/",delete_testimonial,name="delete_testimonial"),
    path("testimonials/<uuid:testimonial_id>/edit/", edit_testimonial, name="edit_testimonial"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path(
        "projects/<uuid:project_id>/star/",
        toggle_star,
        name="toggle_star",
    ),
]