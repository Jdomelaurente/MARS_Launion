from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import StaffSerializer, FileRequestSerializer
from .models import Staff, FileRequest

class RegisterView(generics.CreateAPIView):
    queryset = Staff.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = StaffSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = Staff.objects.get(username=request.data['username'])
            response.data['user'] = {
                'username': user.username,
                'full_name': user.full_name,
                'staff_id': user.staff_id,
                'department': user.department
            }
        return response


import random
import string
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

class FileRequestCreateView(generics.CreateAPIView):
    queryset = FileRequest.objects.all()
    serializer_class = FileRequestSerializer
    permission_classes = (AllowAny,)
    authentication_classes = []

    def generate_unique_code(self):
        while True:
            random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
            code = f"SHS-2026-{random_str}"
            if not FileRequest.objects.filter(request_code=code).exists():
                return code

    def perform_create(self, serializer):
        request_code = self.generate_unique_code()
        instance = serializer.save(request_code=request_code)
        
        # Send Email Notification
        subject = 'Your File Request has been Sent'
        html_content = render_to_string('emails/request_notification.html', {
            'instance': instance,
        })
        text_content = strip_tags(html_content)
        
        from django.conf import settings
        email = EmailMultiAlternatives(
            subject,
            text_content,
            settings.EMAIL_HOST_USER,
            [instance.email]
        )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)



class FileRequestLookupView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []


    def get(self, request, code, *args, **kwargs):
        try:
            file_request = FileRequest.objects.get(request_code=code.upper())
            serializer = FileRequestSerializer(file_request)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except FileRequest.DoesNotExist:
            return Response({'error': 'Invalid request code. No request found.'}, status=status.HTTP_404_NOT_FOUND)
