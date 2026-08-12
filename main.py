# main.py
# SUDARSHAN — Enterprise DAST Engine
# Author: Nilanjan Chowdhury
# GitHub: github.com/CalculusGuy/SUDARSHAN
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import time
import sys
import argparse
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
# ARGPARSE CLI
# ============================================================

def parse_args():
    parser = argparse.ArgumentParser(
        description="SUDARSHAN — Enterprise DAST Engine",
        epilog="Example: python3 main.py --target https://example.com --threads 20"
    )
    parser.add_argument(
        "--target", "-t",
        required=True,
        help="Target URL to scan (e.g., https://example.com)"
    )
    parser.add_argument(
        "--threads", "-th",
        type=int,
        default=10,
        help="Number of threads for concurrent scanning (default: 10)"
    )
    parser.add_argument(
        "--report", "-r",
        choices=["json", "html", "both"],
        default="both",
        help="Report format (default: both)"
    )
    parser.add_argument(
        "--max-pages", "-m",
        type=int,
        default=10,
        help="Maximum number of pages to crawl (default: 10)"
    )
    return parser.parse_args()

# ============================================================
# MAIN
# ============================================================

def main():
    args = parse_args()
    target = args.target
    threads = args.threads
    report_format = args.report
    max_pages = args.max_pages

    print(BANNER)
    print(f"{Fore.CYAN}[*] Target: {target}")
    print(f"{Fore.CYAN}[*] Threads: {threads}")
    print(f"{Fore.CYAN}[*] Report Format: {report_format}")
    print(f"{Fore.CYAN}[*] Max Pages: {max_pages}\n")

    print(f"{Fore.YELLOW}[*] Phase 1: Crawling...")
    pages, forms = crawl(target, max_pages=max_pages)
    print(f"{Fore.GREEN}[+] Found {len(pages)} pages, {len(forms)} forms")

    rules = load_rules()
    if not rules:
        print(f"{Fore.RED}[!] No rules loaded. Exiting.")
        return

    findings = []
    print(f"\n{Fore.YELLOW}[*] Phase 2: Testing URLs...")
    for page in pages[:3]:
        print(f"{Fore.WHITE}[+] Testing: {page}")
        findings.extend(test_url(page, rules))

    print(f"\n{Fore.YELLOW}[*] Testing forms...")
    for form in forms[:3]:
        print(f"{Fore.WHITE}[+] Testing form: {form['action']}")
        findings.extend(test_form(form, rules, target))

    print(f"\n{Fore.YELLOW}[*] Phase 3: Generating reports...")
    if report_format in ["json", "both"]:
        generate_json_report(findings, target)
    if report_format in ["html", "both"]:
        generate_html_report(findings, target)

    print(f"\n{Fore.GREEN}[+] Scan complete! Found {len(findings)} vulnerabilities.")
    print(f"{Fore.CYAN}[+] Reports saved.")
    print(f"{Fore.GREEN}[+] SUDARSHAN — Cuts through web vulnerabilities.")

if __name__ == "__main__":
    main()
