from django.urls import path

from main import api_views

app_name = "api"

urlpatterns = [
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:project_id>/", api_views.project_detail, name="project-detail"),
    path("projects/<uuid:project_id>/star/", api_views.project_star, name="project-star"),
    path("testimonials/", api_views.testimonial_list, name="testimonial-list"),
    path("testimonials/<uuid:testimonial_id>/", api_views.testimonial_detail, name="testimonial-detail"),
    path("testimonials/<uuid:testimonial_id>/heart/", api_views.testimonial_heart, name="testimonial-heart"),
    path("education/", api_views.education_list, name="education-list"),
]