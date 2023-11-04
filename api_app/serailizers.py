from rest_framework import serializers
from django.contrib.auth.models import User
from mainapp.views import Student


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ["id"]
        
        
    def get_selected_fields(self):
        request = self.context.get('request')
        fields = request.query_params.get('data', None)
        if fields:
            fields = fields.split(',')
        return fields
    
    def to_representation(self, instance):
        selected_fields = self.get_selected_fields()
        data = super().to_representation(instance)
        marks_fields = ['marks_hindi', 'marks_english', 'marks_math', 'marks_science', 'marks_grography']
        total_marks = sum(data[field] for field in marks_fields)
        data['total_marks'] = total_marks
        if selected_fields:
            return {key: data[key] for key in selected_fields if key in data}
        return data
    