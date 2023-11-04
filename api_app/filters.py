import django_filters
from mainapp.models import Student

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = {
            'name': ['exact', 'icontains'],
            'roll_no': ['exact'],
            'class_level': ['exact'],
            'marks_hindi': ['exact'],
            'marks_english': ['exact'],
            'marks_math': ['exact'],
            'marks_science': ['exact'],
            'marks_grography': ['exact'],

        }
