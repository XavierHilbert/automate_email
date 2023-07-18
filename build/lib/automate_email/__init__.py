from __future__ import annotations
import platform
if platform.system() == "Windows":
    import win32com.client as win32
else:
    from appscript import app, k

outlook = win32.Dispatch('Outlook.Application') if platform.system() == "Windows" else app('Microsoft Outlook')

def is_internal(email: str) -> bool:
    """Returns true if email is internal, false otherwise."""
    recipient = outlook.createRecipient(email)
    recipient.Resolve()
    if recipient.Resolved:
        return True if recipient.AddressEntry == 0 else False
    else:
        raise Exception(f"Email {email} could not be resolved.")


def send_email(to: list[str], subject: str, body: str, cc: list[str] = [], use_HTML: bool = False, high_priority: bool = False, attachments: list[str] = [], output: str = "SEND") -> None:
    """Constructs and sends an email to the specified recipients."""
    mail = outlook.CreateItem(0)
    mail.to = ';'.join(to)
    mail.cc = ';'.join(cc)
    mail.Importance = 2 if high_priority else 1
    mail.Subject = subject
    for attachment in attachments:
        mail.Attachments.Add(attachment)
    mail.BodyFormat = 2 if use_HTML else 1
    mail.body = body
    mail.Send() if output == "SEND" else mail.Display() if output == "DISPLAY" else mail.Save() if output == "SAVE" else Exception(f"Invalid output option: {output}.")