from rest_framework import serializers
from .models import Personal, Education


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ['degree', 'institution_name', 'passing_year', 'result']


class PersonalSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True)

    class Meta:
        model = Personal
        fields = '__all__'

    def create(self, validated_data):
        educations_data = validated_data.pop('educations')
        student = Personal.objects.create(**validated_data)

        for education_data in educations_data:
            Education.objects.create(student=student, **education_data)

        return student
