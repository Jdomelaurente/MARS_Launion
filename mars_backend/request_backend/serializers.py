from rest_framework import serializers
from .models import Staff, FileRequest

class StaffSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Staff
        fields = ['id', 'username', 'password', 'email', 'staff_id', 'department', 'full_name']

    def create(self, validated_data):
        user = Staff.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', ''),
            staff_id=validated_data['staff_id'],
            department=validated_data.get('department', ''),
            full_name=validated_data['full_name']
        )
        return user


class FileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileRequest
        fields = [
            'id', 'first_name', 'middle_name', 'last_name', 'suffix',
            'sex', 'year_graduated', 'strand', 'birthdate',
            'lrn_number', 'email', 'phone_number', 'permanent_address',
            'requested_files', 'submitted_at', 'status'
        ]
        read_only_fields = ['id', 'submitted_at', 'status']

    def validate_email(self, value):
        if not value.endswith(('.com', '.edu.ph', '.org', '.net')):
            raise serializers.ValidationError("Please provide a valid email address.")
        return value

    def validate_phone_number(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Please provide a valid phone number (at least 10 digits).")
        return value
