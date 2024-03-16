import art
from colorama import Fore, Style

name = input("Enter your name: ")
dream_job = input("Enter your dream job: ")

print("\nYour name in a fancy way: ")
print(Fore.BLUE, end="")
art.tprint(name, font="doh")
print(Style.RESET_ALL)

print("Your dream in a fancy way: ")
print(Fore.RED, end="")
art.tprint(dream_job, font="mscript")
print(Style.RESET_ALL)