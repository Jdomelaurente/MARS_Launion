import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mars_backend.settings')
django.setup()

from django.db import connection
from request_backend.models import Staff

def create_admin():
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        print("Database connection OK")

    username = 'admin'
    password = 'admin'
    email = 'admin@example.com'
    staff_id = 'ADM-001'
    full_name = 'Master Admin'

    try:
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
            print(f"SUCCESS: Admin account created — Username: {username}, Password: {password}")
        else:
            print(f"SUCCESS: Admin account updated — Username: {username}, Password: {password}")

        print(f"  is_staff={staff.is_staff}, is_superuser={staff.is_superuser}, is_active={staff.is_active}")
    except Exception as e:
        print(f"ERROR creating admin: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    create_admin()
