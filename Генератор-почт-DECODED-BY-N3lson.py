#!/usr/bin/env python3 # DECODED BY https://github.com/MrN3lson-Script
# -*- coding: utf-8 -*- # DECODED BY https://github.com/MrN3lson-Script
import os # DECODED BY https://github.com/MrN3lson-Script
import sys # DECODED BY https://github.com/MrN3lson-Script
import json # DECODED BY https://github.com/MrN3lson-Script
import random # DECODED BY https://github.com/MrN3lson-Script
import string # DECODED BY https://github.com/MrN3lson-Script
import requests # DECODED BY https://github.com/MrN3lson-Script
import time # DECODED BY https://github.com/MrN3lson-Script
import smtplib # DECODED BY https://github.com/MrN3lson-Script
from email.mime.text import MIMEText # DECODED BY https://github.com/MrN3lson-Script
# DECODED BY https://github.com/MrN3lson-Script
def generate_username(): # DECODED BY https://github.com/MrN3lson-Script
    length = random.randint(8, 12) # DECODED BY https://github.com/MrN3lson-Script
    chars = string.ascii_lowercase + string.digits # DECODED BY https://github.com/MrN3lson-Script
    return ''.join(random.choices(chars, k=length)) # DECODED BY https://github.com/MrN3lson-Script
# DECODED BY https://github.com/MrN3lson-Script
BANNER = r"""
╔═╗╔═╗╔╗╔╔═╗║ ║  ╔╗ ║ ║╔═╗║═╗
╚═╝╚═╝║║║╚═╝╚═╝  ╚╩═╚═╝╚═╝╩ ╩
 [ Mail Generator & Checker | DECODED BY https://github.com/MrN3lson-Script ]
""" # DECODED BY https://github.com/MrN3lson-Script
# DECODED BY https://github.com/MrN3lson-Script
def test_smtp(acc): # DECODED BY https://github.com/MrN3lson-Script
    try: # DECODED BY https://github.com/MrN3lson-Script
        server = smtplib.SMTP('smtp.1secmaul.com', 587, timeout=10) # DECODED BY https://github.com/MrN3lson-Script
        server.starttls() # DECODED BY https://github.com/MrN3lson-Script
        server.login(acc['login'], acc['password']) # DECODED BY https://github.com/MrN3lson-Script
        server.quit() # DECODED BY https://github.com/MrN3lson-Script
        return "[+] SMTP доступен!" # DECODED BY https://github.com/MrN3lson-Script
    except Exception as e: # DECODED BY https://github.com/MrN3lson-Script
        return f"[-] SMTP ошибка: {str(e)}" # DECODED BY https://github.com/MrN3lson-Script
# DECODED BY https://github.com/MrN3lson-Script
def main(): # DECODED BY https://github.com/MrN3lson-Script
    accounts = [] # DECODED BY https://github.com/MrN3lson-Script
    print(BANNER) # DECODED BY https://github.com/MrN3lson-Script
    # DECODED BY https://github.com/MrN3lson-Script
    while True: # DECODED BY https://github.com/MrN3lson-Script
        print("\n--- ГЛАВНОЕ МЕНЮ ---") # DECODED BY https://github.com/MrN3lson-Script
        print("1. Создать 1 почту (1secmail)") # DECODED BY https://github.com/MrN3lson-Script
        print("2. Создать 5 почт (temp-mail)") # DECODED BY https://github.com/MrN3lson-Script
        print("3. Проверить входящие") # DECODED BY https://github.com/MrN3lson-Script
        print("4. Тест SMTP (проверка валидности)") # DECODED BY https://github.com/MrN3lson-Script
        print("5. Сохранить в JSON") # DECODED BY https://github.com/MrN3lson-Script
        print("0. Выход") # DECODED BY https://github.com/MrN3lson-Script
        # DECODED BY https://github.com/MrN3lson-Script
        choice = input("\nВыберите действие: ") # DECODED BY https://github.com/MrN3lson-Script
        # DECODED BY https://github.com/MrN3lson-Script
        if choice == '1': # DECODED BY https://github.com/MrN3lson-Script
            user = generate_username() # DECODED BY https://github.com/MrN3lson-Script
            domain = "1secmail.com" # DECODED BY https://github.com/MrN3lson-Script
            email = f"{user}@{domain}" # DECODED BY https://github.com/MrN3lson-Script
            accounts.append({ # DECODED BY https://github.com/MrN3lson-Script
                'login': user, # DECODED BY https://github.com/MrN3lson-Script
                'domain': domain, # DECODED BY https://github.com/MrN3lson-Script
                'email': email, # DECODED BY https://github.com/MrN3lson-Script
                'password': generate_username() # DECODED BY https://github.com/MrN3lson-Script
            }) # DECODED BY https://github.com/MrN3lson-Script
            print(f"[+] Создана почта: {email}") # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '2': # DECODED BY https://github.com/MrN3lson-Script
            for _ in range(5): # DECODED BY https://github.com/MrN3lson-Script
                user = generate_username() # DECODED BY https://github.com/MrN3lson-Script
                email = f"{user}@temp-mail.io" # DECODED BY https://github.com/MrN3lson-Script
                accounts.append({ # DECODED BY https://github.com/MrN3lson-Script
                    'login': user, # DECODED BY https://github.com/MrN3lson-Script
                    'domain': "temp-mail.io", # DECODED BY https://github.com/MrN3lson-Script
                    'email': email, # DECODED BY https://github.com/MrN3lson-Script
                    'password': generate_username() # DECODED BY https://github.com/MrN3lson-Script
                }) # DECODED BY https://github.com/MrN3lson-Script
            print("[+] Создано 5 аккаунтов") # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '3': # DECODED BY https://github.com/MrN3lson-Script
            if not accounts: # DECODED BY https://github.com/MrN3lson-Script
                print("[!] Сначала создайте почту") # DECODED BY https://github.com/MrN3lson-Script
                continue # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
            print("\nДоступные аккаунты:") # DECODED BY https://github.com/MrN3lson-Script
            for i, acc in enumerate(accounts, 1): # DECODED BY https://github.com/MrN3lson-Script
                print(f"{i}. {acc['email']}") # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
            try: # DECODED BY https://github.com/MrN3lson-Script
                idx = int(input("\nВыберите номер аккаунта для проверки: ")) - 1 # DECODED BY https://github.com/MrN3lson-Script
                acc = accounts[idx] # DECODED BY https://github.com/MrN3lson-Script
                url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={acc['login']}&domain={acc['domain']}" # DECODED BY https://github.com/MrN3lson-Script
                res = requests.get(url).json() # DECODED BY https://github.com/MrN3lson-Script
                # DECODED BY https://github.com/MrN3lson-Script
                if not res: # DECODED BY https://github.com/MrN3lson-Script
                    print("[-] Писем пока нет.") # DECODED BY https://github.com/MrN3lson-Script
                else: # DECODED BY https://github.com/MrN3lson-Script
                    for msg in res: # DECODED BY https://github.com/MrN3lson-Script
                        print(f"От: {msg['from']} | Тема: {msg['subject']}") # DECODED BY https://github.com/MrN3lson-Script
            except: # DECODED BY https://github.com/MrN3lson-Script
                print("[!] Ошибка выбора") # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '4': # DECODED BY https://github.com/MrN3lson-Script
            if not accounts: # DECODED BY https://github.com/MrN3lson-Script
                print("[!] Нет аккаунтов для теста") # DECODED BY https://github.com/MrN3lson-Script
                continue # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
            for i, acc in enumerate(accounts, 1): # DECODED BY https://github.com/MrN3lson-Script
                print(f"{i}. {acc['email']}") # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
            try: # DECODED BY https://github.com/MrN3lson-Script
                idx = int(input("\nВыберите номер аккаунта: ")) - 1 # DECODED BY https://github.com/MrN3lson-Script
                if 0 <= idx < len(accounts): # DECODED BY https://github.com/MrN3lson-Script
                    acc = accounts[idx] # DECODED BY https://github.com/MrN3lson-Script
                    print(f"\n[+] Тестирование SMTP для {acc['email']}...") # DECODED BY https://github.com/MrN3lson-Script
                    result = test_smtp(acc) # DECODED BY https://github.com/MrN3lson-Script
                    print(result) # DECODED BY https://github.com/MrN3lson-Script
                else: # DECODED BY https://github.com/MrN3lson-Script
                    print("[!] Неверный номер") # DECODED BY https://github.com/MrN3lson-Script
            except: # DECODED BY https://github.com/MrN3lson-Script
                print("[!] Ошибка ввода") # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '5': # DECODED BY https://github.com/MrN3lson-Script
            with open("mails.json", "w") as f: # DECODED BY https://github.com/MrN3lson-Script
                json.dump(accounts, f, indent=4) # DECODED BY https://github.com/MrN3lson-Script
            print("[+] Данные сохранены в mails.json") # DECODED BY https://github.com/MrN3lson-Script
            # DECODED BY https://github.com/MrN3lson-Script
        elif choice == '0': # DECODED BY https://github.com/MrN3lson-Script
            print("Выход...") # DECODED BY https://github.com/MrN3lson-Script
            break # DECODED BY https://github.com/MrN3lson-Script
# DECODED BY https://github.com/MrN3lson-Script
if __name__ == "__main__": # DECODED BY https://github.com/MrN3lson-Script
    main() # DECODED BY https://github.com/MrN3lson-Script
# DECODED BY https://github.com/MrN3lson-Script

