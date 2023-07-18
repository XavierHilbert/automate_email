from __future__ import annotations
import win32com.client as win32

outlook = win32.Dispatch('Outlook.Application')
olNS = outlook.GetNamespace("MAPI")

def is_internal(email: str) -> bool:
    """Returns true if email is internal, false otherwise."""
    recipient = olNS.CreateRecipient(email)
    recipient.Resolve()
    if recipient.Resolved:
        return True if recipient.AddressEntry == 0 else False
    else:
        raise Exception(f"Email {email} could not be resolved.")


def send_email(to: list[str], subject: str, body: str, cc: list[str] = [], use_HTML: bool = False, high_priority: bool = False, save_email: bool = False) -> None:
    """Constructs and sends an email to the specified recipients."""
    mail = outlook.CreateItem(0)
    mail.to = ';'.join(to)
    mail.cc = ';'.join(cc)
    mail.Importance = 2 if high_priority else 1
    mail.Subject = subject
    mail.BodyFormat = 2 if use_HTML else 1
    mail.body = body
    mail.Send() if not save_email else mail.Save()


