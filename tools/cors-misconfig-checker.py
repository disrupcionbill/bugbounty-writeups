#!/usr/bin/env python3

import requests
import sys

def check_cors(target):
    print(f"[*] Probando configuración CORS en: {target}")

    headers = {
        'Origin': 'https://evil.com',
        'User-Agent': 'Mozilla/5.0',
        'Access-Control-Request-Method': 'GET',
    }

    try:
        response = requests.get(target, headers=headers, timeout=10)
        acao = response.headers.get('Access-Control-Allow-Origin')
        acc = response.headers.get('Access-Control-Allow-Credentials')

        if acao:
            print(f"[+] Access-Control-Allow-Origin detectado: {acao}")
            if acao == "*" or "evil.com" in acao:
                print("⚠️ Posible configuración insegura: permite origen malicioso")
        else:
            print("[-] No se detectó encabezado Access-Control-Allow-Origin")

        if acc == "true":
            print("⚠️ El servidor permite credenciales con cualquier origen")
        else:
            print("[-] No se detectó Access-Control-Allow-Credentials: true")

    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Uso: {sys.argv[0]} <URL>")
        sys.exit(1)

    check_cors(sys.argv[1])
