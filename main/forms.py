from django.forms import ChoiceField, ModelForm, TextInput, Textarea, URLInput, Select
from main.models import Education, Experience, Project, Testimonial

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

class TestimonialForm(ModelForm):
    related_experience = ChoiceField(
        choices=[],
        widget=Select(attrs={'class': 'dropdown'})
    )
    
    class Meta:
        model = Testimonial
        fields = [
            "related_experience",
            "message",
            "sender",
            "image_url",
        ]

        labels = {
            "related_experience": "Related Experience/Project/Education",
            "message": "Message",
            "sender": "Sender Name",
            "image_url": "Image URL",
        }

        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Leave a message here...",
                    "rows": 3,
                }
            ),
            "sender": TextInput(
                attrs={
                    "placeholder": "Enter your name/initial/anonymous here...",
                    "maxlength": 30,
                }
            ),
            "image_url": URLInput(
                attrs={
                    "placeholder": "Insert Google Drive link for related image...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        default_choices = [('Others', 'Others')]
        experience_choices = [(experience, experience) for experience in Experience.objects.all()]
        education_choices = [(education, education) for education in Education.objects.all()]
        project_choices = [(project, project) for project in Project.objects.all()]
        self.fields['related_experience'].choices = default_choices + experience_choices + education_choices + project_choices
