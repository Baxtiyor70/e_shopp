import smtplib


def send_email(send_email, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(user='baxtiyorxojaqulov13@gmail.com', password='pzammbaploghsipe')
        server.sendmail(from_addr='baxtiyorxojaqulov13@gmail.com', to_addrs=send_email, msg=message)
        print('Message sent!')

    except Exception as e:
        print(e)


send_email('xojaqulovbaxtiyor13@gmail.com', '654454')
