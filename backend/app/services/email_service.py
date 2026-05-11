"""Email Service"""

import aiosmtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ..config import settings
import logging

logger = logging.getLogger(__name__)


class EmailService:
    """Email sending service"""
    
    @staticmethod
    async def send_email(
        to_email: str,
        subject: str,
        body: str,
        is_html: bool = False
    ) -> bool:
        """
        Send email
        """
        try:
            message = MIMEMultipart()
            message["From"] = settings.SMTP_FROM
            message["To"] = to_email
            message["Subject"] = subject
            
            message.attach(
                MIMEText(body, "html" if is_html else "plain")
            )
            
            async with aiosmtplib.SMTP(
                hostname=settings.SMTP_SERVER,
                port=settings.SMTP_PORT
            ) as smtp:
                await smtp.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
                await smtp.send_message(message)
            
            logger.info(f"Email sent to {to_email}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email: {str(e)}")
            return False
    
    @staticmethod
    async def send_appointment_confirmation(
        user_email: str,
        appointment_data: dict
    ) -> bool:
        """
        Send appointment confirmation email
        """
        subject = "Appointment Confirmation - Hair AI System"
        body = f"""
        <h2>Appointment Confirmed!</h2>
        <p>Your appointment has been confirmed.</p>
        <p>Date: {appointment_data.get('date')}</p>
        <p>Time: {appointment_data.get('time')}</p>
        <p>Stylist: {appointment_data.get('stylist_name')}</p>
        """
        
        return await EmailService.send_email(user_email, subject, body, is_html=True)
