import sys
import os
import colorama
from art import *
import requests
from termcolor import colored
from colorama import Fore, Style

print(colored(text2art ("Phone Number Lookup"), 'blue'))
print(colored('Created By zKaioZ\n\n'.center(60),'red'))
print(Fore.CYAN + Style.NORMAL + "Exemple: +33 {number}")
print ("\n\n")
number = input(Fore.RED + Style.BRIGHT + "Please enter a Phone Number: ")
api = f"http://phone-number-api.com/json/?number={number}" 
info = requests.get(api + "&fields=status,message,numberType,numberValid,carrier,numberCountryCode,continent,countryName,timezone,country,regionName,city,zip,currency,query").json()
sys.stdout.flush()
print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Phone number              : ", info['query'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Valid ?                   : ", info['numberValid'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "ISP                       : ", info['carrier'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Number Type               : ", info['numberType'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Continent                 : ", info['continent'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Country                   : ", info['countryName'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Postal code               : ", info['zip'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Money                     : ", info['currency'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Timezone                  : ", info['timezone'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")

print(Fore.RED + Style.NORMAL + "Number Country Code       : ", info['numberCountryCode'])

print(Fore.RED + Style.BRIGHT + "----------------------------------------------------------------------")
