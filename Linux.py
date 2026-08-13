#!/bin/bash

# =============================================
#  BLACK HAMMER v2.0 - Linux Power Tool
#  ใช้เพื่อการศึกษาเท่านั้น!
# =============================================

clear

# สี
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Banner
echo -e "${RED}"
echo "╔═══════════════════════════════════════════╗"
echo "║   ██████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗║"
echo "║   ██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝║"
echo "║   ██████╔╝███████║███████║██║     █████╔╝ ║"
echo "║   ██╔══██╗██╔══██║██╔══██║██║     ██╔═██╗ ║"
echo "║   ██████╔╝██║  ██║██║  ██║╚██████╗██║  ██╗║"
echo "║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝║"
echo "╚═══════════════════════════════════════════╝"
echo -e "${NC}"
echo -e "${YELLOW}        ⚡ BLACK HAMMER v2.0 ⚡${NC}"
echo -e "${CYAN}     Linux Power Tool - เพื่อการศึกษา${NC}"
echo ""

# เมนูหลัก
while true; do
    echo -e "${GREEN}════════════════════════════════════════${NC}"
    echo -e "${WHITE}[1]${NC} 📡 สแกนเครือข่าย (Ping Sweep)"
    echo -e "${WHITE}[2]${NC} 🔍 สแกนพอร์ตเปิด (Port Scan)"
    echo -e "${WHITE}[3]${NC} 🌐 ตรวจสอบ DNS และ IP"
    echo -e "${WHITE}[4]${NC} 📂 จัดการไฟล์ (สร้าง/ลบ/ย้าย)"
    echo -e "${WHITE}[5]${NC} 🖥️  ดูข้อมูลระบบ"
    echo -e "${WHITE}[6]${NC} 🔥 สร้างไฟล์ข้อความสุ่ม (Stress Test)"
    echo -e "${WHITE}[7]${NC} 🧹 ล้างแคชและไฟล์ขยะ"
    echo -e "${WHITE}[8]${NC} 📦 ติดตั้งเครื่องมือ (nmap, hydra, sqlmap)"
    echo -e "${WHITE}[9]${NC} 💀 จำลอง DDoS (แบบจำลอง)"
    echo -e "${WHITE}[0]${NC} 🚪 ออกจากโปรแกรม"
    echo -e "${GREEN}════════════════════════════════════════${NC}"
    echo -n -e "${YELLOW}เลือกเมนู [0-9]: ${NC}"
    read choice

    case $choice in
        1)
            echo -e "${BLUE}[+] กำลังสแกนเครือข่าย...${NC}"
            read -p "ใส่เครือข่าย (เช่น 192.168.1): " network
            for i in {1..254}; do
                ping -c 1 -W 1 $network.$i > /dev/null 2>&1 && echo -e "${GREEN}✅ $network.$i เปิดอยู่${NC}" &
            done
            wait
            echo -e "${GREEN}[+] สแกนเสร็จ!${NC}"
            ;;
        2)
            echo -e "${BLUE}[+] กำลังสแกนพอร์ต...${NC}"
            read -p "ใส่ IP เป้าหมาย: " target
            echo -e "${CYAN}สแกนพอร์ต 1-1000 บน $target${NC}"
            for port in {1..1000}; do
                (echo >/dev/tcp/$target/$port) >/dev/null 2>&1 && echo -e "${GREEN}✅ พอร์ต $port เปิด${NC}" &
            done
            wait
            echo -e "${GREEN}[+] สแกนเสร็จ!${NC}"
            ;;
        3)
            echo -e "${BLUE}[+] ตรวจสอบ DNS และ IP${NC}"
            read -p "ใส่ Domain หรือ IP: " domain
            echo -e "${CYAN}IP ของ $domain:${NC}"
            dig +short $domain
            echo -e "${CYAN}Whois:${NC}"
            whois $domain | head -10
            ;;
        4)
            echo -e "${BLUE}[+] จัดการไฟล์${NC}"
            echo "[1] สร้างไฟล์"
            echo "[2] ลบไฟล์"
            echo "[3] ย้ายไฟล์"
            read -p "เลือก: " sub
            case $sub in
                1) read -p "ชื่อไฟล์: " f; touch "$f"; echo -e "${GREEN}✅ สร้าง $f${NC}";;
                2) read -p "ชื่อไฟล์: " f; rm -i "$f";;
                3) read -p "ไฟล์ต้นทาง: " src; read -p "ปลายทาง: " dst; mv "$src" "$dst"; echo -e "${GREEN}✅ ย้ายแล้ว${NC}";;
                *) echo -e "${RED}❌ ไม่ถูกต้อง${NC}";;
            esac
            ;;
        5)
            echo -e "${BLUE}[+] ข้อมูลระบบ${NC}"
            echo -e "${CYAN}OS:${NC} $(uname -a)"
            echo -e "${CYAN}CPU:${NC} $(lscpu | grep 'Model name' | head -1)"
            echo -e "${CYAN}RAM:${NC} $(free -h | grep Mem | awk '{print $3 "/" $2}')"
            echo -e "${CYAN}ดิสก์:${NC} $(df -h / | awk 'NR==2{print $3 "/" $2}')"
            ;;
        6)
            echo -e "${BLUE}[+] สร้างไฟล์ข้อความสุ่ม 1000 บรรทัด${NC}"
            read -p "ชื่อไฟล์: " f
            for i in {1..1000}; do
                echo "Line $i - $(date) - รหัส: $(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | head -c 10)" >> $f
            done
            echo -e "${GREEN}✅ สร้าง $f เรียบร้อย (1000 บรรทัด)${NC}"
            ;;
        7)
            echo -e "${BLUE}[+] ล้างแคชและไฟล์ขยะ${NC}"
            echo -e "${YELLOW}🗑️  กำลังลบไฟล์ชั่วคราว...${NC}"
            rm -rf /tmp/* 2>/dev/null
            rm -rf ~/.cache/* 2>/dev/null
            echo -e "${GREEN}✅ ล้างเสร็จ!${NC}"
            ;;
        8)
            echo -e "${BLUE}[+] ติดตั้งเครื่องมือ${NC}"
            echo -e "${YELLOW}กำลังติดตั้ง nmap, hydra, sqlmap...${NC}"
            if command -v pkg &>/dev/null; then
                pkg install nmap hydra sqlmap -y
            elif command -v apt &>/dev/null; then
                sudo apt update && sudo apt install nmap hydra sqlmap -y
            else
                echo -e "${RED}❌ ไม่รู้จักระบบแพ็กเกจ${NC}"
            fi
            echo -e "${GREEN}✅ ติดตั้งเสร็จ!${NC}"
            ;;
        9)
            echo -e "${BLUE}[+] จำลอง DDoS (เพื่อการศึกษา)${NC}"
            read -p "ใส่ IP เป้าหมาย (ของคุณเอง): " target
            echo -e "${RED}⚠️  เริ่มจำลองการโจมตี $target (กด Ctrl+C เพื่อหยุด)${NC}"
            for i in {1..50}; do
                echo -e "${YELLOW}📡 ส่งแพ็กเก็ต $i ไปยัง $target${NC}"
                sleep 0.1
            done
            echo -e "${GREEN}✅ จำลองเสร็จ!${NC}"
            ;;
        0)
            echo -e "${RED}🚪 ออกจาก BLACK HAMMER...${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}❌ เลขไม่ถูกต้อง! ลองใหม่${NC}"
            ;;
    esac
    echo ""
    echo -e "${CYAN}กด Enter เพื่อกลับเมนู...${NC}"
    read
    clear
done
