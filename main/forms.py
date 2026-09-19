from django.forms import ModelForm, TextInput, Textarea, URLInput
from main.models import Project 

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "tech_stack",
            "project_url",
            "project_image_url",
        ]

        labels = {
            "title": "Project Name",
            "description": "Project Description",
            "tech_stack": "Tech Stack Used for Project",
            "project_url": "Project URL",
            "project_image_url": "Project Image URL",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Website name...",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Tell a story about your website...",
                    "rows": 3,
                }
            ),
            "tech_stack": TextInput(
                attrs={
                    "placeholder": "Tech stacks used for development...",
                }
            ),
            "project_url": URLInput(
                attrs={
                    "placeholder": "Insert GitHub link for the project...",
                }
            ),
            "project_image_url": URLInput(
                attrs={
                    "placeholder": "Insert Google Drive link for the project image...",
                }
            ),
        }