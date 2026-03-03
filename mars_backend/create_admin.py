import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mars_backend.settings')
django.setup()

from request_backend.models import Staff

def create_admin():
    username = 'admin'
    password = 'admin_password123'
    email = 'admin@example.com'
    staff_id = 'ADM-001'
    full_name = 'Master Admin'

    staff, created = Staff.objects.get_or_create(username=username, defaults={
        'email': email,
        'staff_id': staff_id,
        'full_name': full_name,
        'is_staff': True,
        'is_superuser': True,
    })

    staff.set_password(password)
    staff.is_staff = True
    staff.is_superuser = True
    staff.save()
    
    if created:
        print(f"Admin account created: Username: {username}, Password: {password}")
    else:
        print(f"Admin account updated: Username: {username}, Password: {password}")

if __name__ == '__main__':
    create_admin()
