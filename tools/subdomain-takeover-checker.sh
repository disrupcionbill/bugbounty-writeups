#!/bin/bash

# ✅ Requiere: dig, host

if [ -z "$1" ]; then
  echo "Uso: $0 <archivo_de_subdominios.txt>"
  exit 1
fi

echo "[*] Escaneando posibles subdomain takeovers..."

while read -r sub; do
  cname=$(dig +short CNAME "$sub")
  if [ -n "$cname" ]; then
    echo "[+] $sub -> $cname"
    host "$cname" | grep "NXDOMAIN" >/dev/null && echo "   ⚠️  Posible takeover: $cname"
  fi
done < "$1"
