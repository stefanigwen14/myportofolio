from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Education

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            # sementara utk tutorial tdk menambahkan tahun masuk/lulus krn formatnya datetime
            "institution",
            "major",
            "activities",
            "achievements",
        ]

        labels = {
            "institution": "Institusi Pendidikan",
            "major": "Jurusan",
            "activities": "Aktivitas",
            "achievements": "Pencapaian",
        }

        widgets = {
            "institution": TextInput(
                attrs={
                    "placeholder": "Institusi Pendidikan",
                    "maxlength": 255,
                }
            ),
            "major": TextInput(
                attrs={
                    "placeholder": "Jurusan",
                    "maxlength": 255,
                }
            ),
            "activities": Textarea(
                attrs={
                    "placeholder": "Aktivitas",
                    "rows": 3,
                }
            ),
            "achievements": Textarea(
                attrs={
                    "placeholder": "Pencapaian",
                    "rows": 3,
                }
            ),
        }