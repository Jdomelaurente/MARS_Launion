from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Staff, FileRequest, Strand, DocumentType, PickupSlot, AuditLog, ProcessedDocument

@admin.register(ProcessedDocument)
class ProcessedDocumentAdmin(admin.ModelAdmin):
    list_display = ['document_type', 'request', 'uploaded_by', 'uploaded_at']
    search_fields = ['document_type', 'request__first_name', 'request__last_name']
    list_filter = ['document_type', 'uploaded_at']


@admin.register(Strand)
class StrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']

class StaffAdmin(UserAdmin):
    model = Staff
    list_display = ['username', 'email', 'full_name', 'staff_id', 'department', 'is_staff', 'is_active']
    search_fields = ['username', 'full_name', 'email', 'staff_id']
    list_filter = ['department', 'is_staff', 'is_superuser', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        ('Staff Info', {'fields': ('staff_id', 'department', 'full_name')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Staff Info', {'fields': ('staff_id', 'department', 'full_name')}),
    )

admin.site.register(Staff, StaffAdmin)


@admin.register(FileRequest)
class FileRequestAdmin(admin.ModelAdmin):
    list_display = [
        'full_name_display', 'email', 'phone_number',
        'year_graduated', 'strand', 'status', 'submitted_at',
        'display_requested_files'
    ]
    list_filter = ['status', 'sex', 'strand', 'year_graduated', 'submitted_at']
    search_fields = ['first_name', 'last_name', 'email', 'lrn_number', 'phone_number']
    readonly_fields = ['submitted_at']
    ordering = ['-submitted_at']
    actions = ['mark_as_approved', 'mark_as_rejected', 'mark_as_processing']

    def full_name_display(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name_display.short_description = 'Name'

    def display_requested_files(self, obj):
        if isinstance(obj.requested_files, list):
            return ", ".join(obj.requested_files)
        return str(obj.requested_files)
    display_requested_files.short_description = 'Requested Files'

    @admin.action(description='Mark selected requests as Approved')
    def mark_as_approved(self, request, queryset):
        queryset.update(status='Approved')

    @admin.action(description='Mark selected requests as Rejected')
    def mark_as_rejected(self, request, queryset):
        queryset.update(status='Rejected')

    @admin.action(description='Mark selected requests as Processing')
    def mark_as_processing(self, request, queryset):
        queryset.update(status='Processing')
