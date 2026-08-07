# main.py
# SUDARSHAN — Enterprise DAST Engine
# Author: Nilanjan Chowdhury
# GitHub: github.com/CalculusGuy/SUDARSHAN

import json
import time
import sys
from crawler.crawler import crawl
from engine.engine import test_url, test_form
from reporter.reporter import generate_json_report, generate_html_report
from colorama import init, Fore, Style

init(autoreset=True)

# ============================================================
# ASCII BANNER — SUDARSHAN
# ============================================================

BANNER = f"""
{Fore.CYAN}{Style.BRIGHT}
   ███████╗██╗   ██╗██████╗  █████╗ ███████╗██╗  ██╗ █████╗ ███╗   ██╗
   ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝██║  ██║██╔══██╗████╗  ██║
   ███████╗██║   ██║██████╔╝███████║███████╗███████║███████║██╔██╗ ██║
   ╚════██║██║   ██║██╔══██╗██╔══██║╚════██║██╔══██║██╔══██║██║╚██╗██║
   ███████║╚██████╔╝██████╔╝██║  ██║███████║██║  ██║██║  ██║██║ ╚████║
   ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
{Fore.GREEN}   Enterprise DAST Engine for Modern Web Applications
{Fore.YELLOW}   Cuts through web vulnerabilities.
{Fore.WHITE}   Author: Nilanjan Chowdhury
{Fore.CYAN}   GitHub: github.com/CalculusGuy/SUDARSHAN
{Style.RESET_ALL}
"""

# ============================================================
# PROGRESS SPINNER
# ============================================================

def spinner(message):
    chars = "|/-\\"
    for char in chars:
        sys.stdout.write(f"\r{Fore.YELLOW}[*] {message} {char}")
        sys.stdout.flush()
        time.sleep(0.1)

# ============================================================
# LOAD RULES
# ============================================================

def load_rules():
    try:
        with open("rules/dast_rules.json", "r") as f:
            data = json.load(f)
        print(f"{Fore.GREEN}[+] Loaded {len(data['rules'])} rules")
        return data["rules"]
    except FileNotFoundError:
        print(f"{Fore.RED}[!] rules/dast_rules.json not found.")
        return []

# ============================================================
# MAIN
# ============================================================

def main():
    print(BANNER)
    
    target = input(f"{Fore.CYAN}[?] Enter target URL: {Fore.WHITE}")

    print(f"\n{Fore.YELLOW}[*] Scanning: {target}")
    spinner("Crawling pages")
    pages, forms = crawl(target, max_pages=10)
    print(f"\r{Fore.GREEN}[+] Found {len(pages)} pages, {len(forms)} forms")

    rules = load_rules()
    if not rules:
        print(f"{Fore.RED}[!] No rules loaded. Exiting.")
        return

    findings = []
    print(f"\n{Fore.YELLOW}[*] Testing URLs...")
    for page in pages[:3]:
        print(f"{Fore.WHITE}[+] Testing: {page}")
        findings.extend(test_url(page, rules))

    print(f"\n{Fore.YELLOW}[*] Testing forms...")
    for form in forms[:3]:
        print(f"{Fore.WHITE}[+] Testing form: {form['action']}")
        findings.extend(test_form(form, rules, target))

    generate_json_report(findings, target)
    generate_html_report(findings, target)

    print(f"\n{Fore.GREEN}[+] Scan complete! Found {len(findings)} vulnerabilities.")
    print(f"{Fore.CYAN}[+] Reports saved to scan_report.json and scan_report.html")
    print(f"{Fore.GREEN}[+] SUDARSHAN — Cuts through web vulnerabilities.")

if __name__ == "__main__":
    main()
