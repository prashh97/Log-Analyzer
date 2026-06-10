# 📄Log analyzer for web servers

this is a simple Python CLI tool for analyzing Apache and Nginx access logs. The analyzer extracts visitor statistics, HTTP status code distributions, frequently accessed pages, and error events, generating a summary report for further investigation.

## Features

* Parses standard Apache/Nginx access log format
* Shows total requests and unique visitor IPs
* Breaks down HTTP status codes (200, 301, 404, 500, etc.)
* Lists the top 5 most active IP addresses
* Lists the top 5 most visited pages
* Detects and displays all error responses (4xx / 5xx)
* Generates and saves a summary report to `report.txt`

## Requirements

* Python 3
* No external libraries required (uses only Python built-in modules)

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/prashh97/web-log-analyzer.git
cd log-analyzer
```

### 2. Run the Analyzer

```bash
python log_analyzer.py
```

Enter the log file name when prompted:

```text
Enter log file name: access.log
```

## Sample Output

```text
=============================================
         LOG FILE ANALYSIS REPORT
=============================================
  Total Requests : 982
  Unique IPs     : 9
  Total Errors   : 204

--- Status Codes ---
  200  →  648 times
  404  →  166 times
  500  →  20 times

--- Top 5 Visitors (by IP) ---
  198.51.100.7         167 requests
  203.0.113.45         160 requests

--- Top 5 Visited Pages ---
  85     /images/logo.png
  77     /

--- Errors (4xx / 5xx) ---
  [404] GET /old-link  (from 10.0.0.5)
  [500] GET /api/heavy (from 192.168.1.22)

  Report saved to report.txt
=============================================
```

## Supported Log Format

The analyzer supports standard Apache Combined Log Format and Nginx access logs.

Example:

```text
127.0.0.1 - - [10/Jun/2024:12:00:00 +0000] "GET /index.html HTTP/1.1" 200 1234 "-" "Mozilla/5.0"
```

## Project Structure

| File                     | Description                               |
| ------------------------ | ----------------------------------------- |
| `log_analyzer.py`        | Main analyzer script                      |
| `generate_sample_log.py` | Generates sample log files for testing    |
| `report.txt`             | Analysis report generated after execution |

## Future Improvements

* Brute-force login detection
* Suspicious IP activity detection
* CSV and JSON export support
* Interactive web dashboard
* Threat intelligence integration
* IP geolocation lookups

## Author

Built as part of my cybersecurity learning journey, with a focus on log analysis, security monitoring, and Python-based automation.

Feedback, suggestions, and contributions are always welcome.
