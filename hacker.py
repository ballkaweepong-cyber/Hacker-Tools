#!/usr/bin/env python3

import os
import sys
import subprocess

# สี
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
NC = '\033[0m'

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(RED + """
╔═══════════════════════════════════════════╗
║   ██████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗║
║   ██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝║
║   ██████╔╝███████║███████║██║     █████╔╝ ║
║   ██╔══██╗██╔══██║██╔══██║██║     ██╔═██╗ ║
║   ██████╔╝██║  ██║██║  ██║╚██████╗██║  ██╗║
║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝║
╚═══════════════════════════════════════════╝
""" + NC)
    print(YELLOW + "        ⚡ HACKER TOOL v1.0 ⚡" + NC)
    print(BLUE + "     Linux Power Tool - เพื่อการศึกษา" + NC)
    print("")

def scan_network():
    network = input("ใส่เครือข่าย (เช่น 192.168.1): ")
    print(GREEN + "[+] กำลังสแกน..." + NC)
    for i in range(1, 255):
        ip = f"{network}.{i}"
        response = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        if response == 0:
            print(GREEN + f"✅ {ip} เปิดอยู่" + NC)

def scan_port():
    target = input("ใส่ IP เป้าหมาย: ")
    print(GREEN + "[+] กำลังสแกนพอร์ต 1-1000..." + NC)
    for port in range(1, 1001):
        result = os.system(f"echo >/dev/tcp/{target}/{port} 2>/dev/null")
        if result == 0:
            print(GREEN + f"✅ พอร์ต {port} เปิด" + NC)

def system_info():
    print(CYAN + "OS:" + NC, os.uname().sysname)
    print(CYAN + "Hostname:" + NC, os.uname().nodename)
    print(CYAN + "CPU:" + NC, os.uname().machine)

def main():
    while True:
        banner()
        print(GREEN + "════════════════════════════════════════" + NC)
        print("[1] 📡 สแกนเครือข่าย")
        print("[2] 🔍 สแกนพอร์ต")
        print("[3] 🖥️  ดูข้อมูลระบบ")
        print("[0] 🚪 ออก")
        print(GREEN + "════════════════════════════════════════" + NC)
        choice = input(YELLOW + "เลือก [0-3]: " + NC)

        if choice == "1":
            scan_network()
        elif choice == "2":
            scan_port()
        elif choice == "3":
            system_info()
        elif choice == "0":
            print(RED + "🚪 ออก..." + NC)
            break
        else:
            print(RED + "❌ เลขไม่ถูกต้อง" + NC)

        input("กด Enter เพื่อกลับเมนู...")

if __name__ == "__main__":
    main()
