# alert/alert.py

import smtplib
from email.mime.text import MIMEText

# Configuration
ALERT_THRESHOLD = 10  # Number of harmful contents before alerting
HARMFUL_COUNT = 12    # This would normally be computed dynamically

# Email settings
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_password'
FROM_EMAIL = 'your_email@example.com'
TO_EMAIL = 'trusted_contact@example.com'

def send_alert(harmful_count):
    subject = "Alert: High Harmful Content Detected"
    body = f"The system has detected {harmful_count} instances of harmful content. Immediate attention is required."
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = TO_EMAIL

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(FROM_EMAIL, [TO_EMAIL], msg.as_string())
        server.quit()
        print("Alert sent successfully.")
    except Exception as e:
        print("Failed to send alert:", e)

if __name__ == '__main__':
    if HARMFUL_COUNT >= ALERT_THRESHOLD:
        send_alert(HARMFUL_COUNT)
    else:
        print("Harmful content count is below the threshold.")
