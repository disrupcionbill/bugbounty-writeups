#!/bin/bash

TOOLS_DIR="./tools"
WRITEUPS_DIR="./"
GITHUB_BRANCH="main"

menu() {
  clear
  echo "🚀 Disrupción Bill Offensive Toolkit"
  echo "------------------------------------"
  echo "1. Ejecutar Bypass 403"
  echo "2. Ejecutar CORS Misconfig Checker"
  echo "3. Crear nuevo writeup SSRF"
  echo "4. Subir cambios a GitHub"
  echo "5. Salir"
  echo ""
  read -p "Selecciona una opción: " option
}

run_bypass_403() {
  read -p "URL a testear: " url
  python3 $TOOLS_DIR/bypass-403.py "$url"
}

run_cors_checker() {
  read -p "URL a testear: " url
  bash $TOOLS_DIR/cors-checker.sh "$url"
}

create_writeup_ssrf() {
  read -p "Nombre del archivo (sin .md): " name
  mkdir -p ssrf
  FILE="ssrf/$name.md"

  cat <<EOF > "$FILE"
---
title: SSRF - $name
tags: [ssrf, bugbounty]
author: Disrupción Bill
---

## 💥 Prueba de concepto

\`\`\`bash
curl "https://target.com/proxy?url=http://127.0.0.1:8000/status"
\`\`\`

## 🧠 Explicación

Este SSRF permite interactuar con servicios internos gracias a un endpoint proxy sin validación.

## ✅ Impacto

- Acceso a servicios internos.
- Enumeración de APIs.
EOF

  git add "$FILE"
  git commit -m "Automated writeup: SSRF $name"
  git push origin $GITHUB_BRANCH
  echo "✅ SSRF guardado y subido: $FILE"
}

push_to_github() {
  git add .
  git commit -m "Update from toolkit"
  git push origin $GITHUB_BRANCH
}

while true; do
  menu
  case $option in
    1) run_bypass_403 ;;
    2) run_cors_checker ;;
    3) create_writeup_ssrf ;;
    4) push_to_github ;;
    5) exit ;;
    *) echo "Opción inválida." ;;
  esac
  echo ""
  read -p "Presiona Enter para continuar..." temp
done
