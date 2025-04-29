import requests
from bs4 import BeautifulSoup
from googlesearch import search
import re
import os

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 10)"
}

def banner():
    os.system("clear")
    print("""
    \033[1;32m
     ██████╗  ██████╗  ██████╗  ██████╗ ██╗     ██╗██████╗ 
    ██╔════╝ ██╔═══██╗██╔════╝ ██╔════╝ ██║     ██║██╔══██╗
    ██║  ███╗██║   ██║██║  ███╗██║  ███╗██║     ██║██████╔╝
    ██║   ██║██║   ██║██║   ██║██║   ██║██║     ██║██╔═══╝ 
    ╚██████╔╝╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║██║     
     ╚═════╝  ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝╚═╝     
     \033[1;37m
       0xGolip-Team Tools VIP  |  Email OSINT Recon
       Cyber Weapon for Social Engineers & InfoSec
    --------------------------------------------------------
    """)

def google_search(target):
    print(f"\033[1;36m[+] Searching Google for target: {target}\033[0m")
    queries = [
        f'"{target}" email',
        f'"{target}" contact',
        f'"{target}" site:pastebin.com',
        f'"{target}" site:github.com',
        f'"{target}" site:archive.org',
        f'"{target}" site:telegram.me',
    ]
    urls = set()
    for query in queries:
        try:
            for result in search(query, num_results=10):
                urls.add(result)
        except Exception as e:
            print(f"\033[1;31m[-] Google error: {e}\033[0m")
    return list(urls)

def extract_emails_from_url(url):
    try:
        r = requests.get(url, headers=headers, timeout=7)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.get_text()
        emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
        return set(emails)
    except Exception:
        return set()

def run_osint(target):
    urls = google_search(target)
    found_emails = set()
    for url in urls:
        print(f"\033[1;34m    [*] Scraping: {url}\033[0m")
        emails = extract_emails_from_url(url)
        found_emails.update(emails)
    return found_emails

if __name__ == "__main__":
    banner()
    target = input("\033[1;33m[?] Masukkan Nama / Username / Nomor HP: \033[0m")
    print("\n\033[1;37m[=] Proses intelijen dimulai... tunggu...\033[0m\n")
    emails = run_osint(target)
    if emails:
        print(f"\n\033[1;32m[+] Email ditemukan ({len(emails)} total):\033[0m")
        for email in emails:
            print(f"   \033[1;37m> {email}\033[0m")
    else:
        print("\033[1;31m[-] Tidak ada email ditemukan.\033[0m")

    print("\n\033[1;35m[✓] Proses selesai. Dibantu oleh 0xGolip-Team Tools VIP.\033[0m")
