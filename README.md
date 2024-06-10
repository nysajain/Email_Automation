# Email Automation Script in Python

This repository contains a simple Python script for automating the process of sending emails using the `smtplib` library. The script is designed to send an email from a specified sender's email address to a recipient's email address with a given subject and body text. 

## Features

- **SMTP Integration**: Uses `smtplib` to handle email sending through Gmail's SMTP server.
- **Email Composition**: Utilizes `email.mime.text.MIMEText` and `email.mime.multipart.MIMEMultipart` to create the email's body and subject.
- **User Input**: Prompts the user for the recipient's email address, subject, and body of the email.
- **Secure Connection**: Establishes a secure connection to the SMTP server using TLS.

## Prerequisites

- Python 3.x
- An active Gmail account
- Access to Gmail's SMTP server (make sure "Less secure app access" is enabled in your Gmail account settings)

## Usage

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/email-automation.git
    cd email-automation
    ```

2. **Update the sender's email credentials**:
    - Replace the `sender_emailID` and `password` variables in the script with your Gmail address and app password. For better security, consider using environment variables or input prompts.

3. **Run the script**:
    ```sh
    python send_email.py
    ```

4. **Follow the prompts**:
    - Enter the recipient's email address.
    - Enter the subject of the email.
    - Enter the body of the email.

## Notes

- Ensure you have enabled "Less secure app access" in your Gmail account settings or use an app-specific password if 2-step verification is enabled.
