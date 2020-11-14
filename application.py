import time
from datetime import datetime as dt

host_path = "C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"

website_list = [
    "www.facebook.com",
    "www.gmail.com"
]

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt(dt.now().year, dt.now().month, dt.now().day, 19):
        # This condition just impleies while the time is within 9 to 6pm perfrom this function
        with open(host_path, "r+") as file:
            content = file.read()
            for website in website_list:
                if(website in content):
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

            print("all the listed sites are blocked")
            break
    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Websites are unblocked have fun!")
        break
