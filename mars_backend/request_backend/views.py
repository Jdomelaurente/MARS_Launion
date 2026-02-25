from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
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


class FileRequestCreateView(generics.CreateAPIView):
    queryset = FileRequest.objects.all()
    serializer_class = FileRequestSerializer
    permission_classes = (AllowAny,)
