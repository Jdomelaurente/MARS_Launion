from django.core.mail import send_mail
from django.conf import settings

def send_request_notification(request_obj):
    """
    Sends an email notification to the student based on the status of their request.
    """
    subject = ""
    message = ""
    status = request_obj.status
    
    # Base message template
    header = f"Dear {request_obj.first_name} {request_obj.last_name},\n\n"
    footer = f"\n\nPass Key: {request_obj.passkey}\nScheduled Pickup: {request_obj.pickup_date} @ {request_obj.pickup_time}\n\nThank you,\nLa Union SHS Administration"

    if status == 'Approved':
        subject = "Document Request Approved - La Union SHS"
        message = (
            f"{header}Your request for documents has been APPROVED. "
            f"Please prepare the necessary payment and documents for your scheduled pickup."
            f"{footer}"
        )
    elif status == 'Completed':
        subject = "Document Request Released - La Union SHS"
        message = (
            f"{header}Your requested documents have been RELEASED and the transaction is now marked as Completed. "
            f"Thank you for using our digital portal.{footer}"
        )
    elif status == 'Needs Verification':
        subject = "Action Required: Missing Record - La Union SHS"
        message = (
            f"{header}Your request for documents is currently on hold. We could not find a digital copy of your master record in our database. "
            f"Our staff is currently conducting a manual search of our physical archives. No action is required from you at this time."
            f"{footer}"
        )
    elif status == 'Rejected':
        subject = "Document Request Update - La Union SHS"
        message = (
            f"{header}We regret to inform you that your document request has been REJECTED. "
            f"Please contact the school office for more details.\n\nRegards,\nLa Union SHS Administration"
        )
    else:
        # Don't send email for other statuses unless needed
        return

    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, # Sender
            [request_obj.email],      # Recipient
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Email failed: {e}")
        return False
