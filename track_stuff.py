import requests
import smtplib
from bs4 import BeautifulSoup
import time

url = "https://www.amazon.co.uk/dp/B07K6H583G/?coliid=ILF3LQY0QDM0S&colid=1JTQ8MQFGDJJI&psc=1&ref_=lv_ov_lig_dp_it"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}


def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    price = soup.find(id="priceblock_ourprice").get_text()
    strip_price = price[1:6]
    replaced_str = strip_price.replace(",", ".")
    final_price = float(replaced_str)

    if final_price <= 1.200:
        print("The price target has been hit!\nSending email now.")
        send_email()
    else:
        print("Price has not reached the desired level.\nWill check again in 12 hours.")

# Create an instance of an SMTP server to facilitate the sending of emails
def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("balinski.n@gmail.com", "password")
# Creates the subject and body of the email
    subject = "PRICE ALERT!!! - VGA GeForce RTX 2080 Ti FTW3 ULTRA GAMING"
    body = "Follow the link: https://www.amazon.co.uk/dp/B07K6H583G/?coliid=ILF3LQY0QDM0S&colid=1JTQ8MQFGDJJI&psc=1&ref_=lv_ov_lig_dp_it"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail("balinski.n@gmail.com", "son1k@protonmail.com", msg)
# Kill the server.
    server.quit()

check_price()

# Can run as a background process or schedule through cron.
"""while True:
    check_price()
    time.sleep(43200)"""
# adding a comment for testing
