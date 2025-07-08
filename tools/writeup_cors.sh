#!/bin/bash

mkdir -p ../cors

cat > ../cors/wildcard-origin.md << 'EOF'
---
title: "CORS con origen comodín *"
severity: Medium
tags: [CORS, misconfiguration, web]
---

## 🧠 Descripción

El endpoint permite solicitudes cross-origin desde cualquier origen (`*`).  
Esto puede permitir a un atacante leer respuestas desde un dominio malicioso si no hay validación del origen.

## 💥 Prueba de concepto

```bash
curl -i -H "Origin: https://evil.com" https://victima.com/api
