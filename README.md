# automate_email 

pip install autoamte_email
import automate_email as auto_email

## Example code for is_internal

is_internal returns true if there is an email exists and that the email is internal and false otherwise. Given that I am signed into my unc account on Outlook, theese are the results.

auto_email.is_internal("email@ad.unc.edu") => True
auto_email.is_internal("email_not_in_unc_directory@ad.unc.edu") => False
auto_email.is_internal("email@gmail.com") => False

## Example code for send_email

message = "Dear X,<br><br>\
          This is a <b>test</b>.<br><br>\
          Best,<br>
          Y"
auto_email.send_email(to = [email@ad.unc.edu], subject= "SUBJECT, body = message, use_HTML = True, high_priority = True)

*** Only works for windows currently ***
