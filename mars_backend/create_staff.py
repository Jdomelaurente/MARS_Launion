import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mars_backend.settings')
django.setup()

from request_backend.models import Staff
try:
    if not Staff.objects.filter(username='staff1').exists():
        Staff.objects.create_user(
            username='staff1', 
            password='Password123!', 
            email='staff1@example.com', 
            staff_id='S-2024-001', 
            department='Registrar', 
            full_name='Test Staff'
        )
        print("Staff account 'staff1' created successfully.")
    else:
        print("Staff account 'staff1' already exists.")
except Exception as e:
    print(f"Error: {e}")
