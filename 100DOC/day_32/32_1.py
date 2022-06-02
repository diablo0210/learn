#   How to send emails with Python using SMTP

import smtplib

my_email = "07bt1008@gmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password="kgpkarollnumber")
    connection.sendmail(
        from_addr=my_email,
        to_addrs="viveksharma0210@yahoo.com",
        msg="Subject: Hello\n\n Hope you are ok.\n I heard about the diagnosis."
    )
