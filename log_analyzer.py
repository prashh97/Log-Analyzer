# Simple Log File Analyzer
# Works with Apache/Nginx log files

import re
from collections import Counter

def analyze_log(filename):
    # Pattern to read each log line
    pattern = re.compile(r'(\S+) .+ \[(.+?)\] "(\S+) (\S+) \S+" (\d+) (\S+)')

    ips = []
    pages = []
    status_codes = []
    total_lines = 0
    errors = []

    print(f"\nReading file: {filename}\n")

    with open(filename, 'r') as f:
        for line in f:
            match = pattern.match(line)
            if match:
                ip     = match.group(1)
                method = match.group(3)
                page   = match.group(4)
                status = match.group(5)

                ips.append(ip)
                pages.append(page)
                status_codes.append(status)
                total_lines += 1

                # Collect errors (4xx and 5xx)
                if status.startswith('4') or status.startswith('5'):
                    errors.append((ip, method, page, status))

    if total_lines == 0:
        print("No valid log entries found.")
        return

    #  Summary 
    print("=" * 45)
    print("         LOG FILE ANALYSIS REPORT")
    print("=" * 45)
    print(f"  Total Requests : {total_lines}")
    print(f"  Unique IPs     : {len(set(ips))}")
    print(f"  Total Errors   : {len(errors)}")

    #  Status Codes 
    print("\n--- Status Codes ---")
    for code, count in sorted(Counter(status_codes).items()):
        print(f"  {code}  →  {count} times")

    #  Top 5 IPs 
    print("\n--- Top 5 Visitors (by IP) ---")
    for ip, count in Counter(ips).most_common(5):
        print(f"  {ip:<20} {count} requests")

    #  Top 5 Pages 
    print("\n--- Top 5 Visited Pages ---")
    for page, count in Counter(pages).most_common(5):
        print(f"  {count:<6} {page}")

    #  Errors 
    print("\n--- Errors (4xx / 5xx) ---")
    if errors:
        for ip, method, page, status in errors[:10]:
            print(f"  [{status}] {method} {page}  (from {ip})")
        if len(errors) > 10:
            print(f"  ... and {len(errors) - 10} more errors")
    else:
        print("  No errors found!")

    #  Save to report.txt 
    with open("report.txt", "w") as f:
        f.write("LOG FILE ANALYSIS REPORT\n")
        f.write("=" * 45 + "\n")
        f.write(f"Total Requests : {total_lines}\n")
        f.write(f"Unique IPs     : {len(set(ips))}\n")
        f.write(f"Total Errors   : {len(errors)}\n\n")
        f.write("Status Codes:\n")
        for code, count in sorted(Counter(status_codes).items()):
            f.write(f"  {code} -> {count}\n")
        f.write("\nTop 5 IPs:\n")
        for ip, count in Counter(ips).most_common(5):
            f.write(f"  {ip} - {count} requests\n")
        f.write("\nTop 5 Pages:\n")
        for page, count in Counter(pages).most_common(5):
            f.write(f"  {count} - {page}\n")
        f.write("\nErrors:\n")
        for ip, method, page, status in errors:
            f.write(f"  [{status}] {method} {page} from {ip}\n")

    print("\n  Report saved to report.txt")
    print("=" * 45)



filename = input("Enter log file name: ")
analyze_log(filename)
