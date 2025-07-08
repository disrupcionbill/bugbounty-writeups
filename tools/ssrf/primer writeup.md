---
title: SSRF - primer writeup
tags: [ssrf, bugbounty]
author: Disrupción Bill
---

## 💥 Prueba de concepto

```bash
curl "https://target.com/proxy?url=http://127.0.0.1:8000/status"
```

## 🧠 Explicación

Este SSRF permite interactuar con servicios internos gracias a un endpoint proxy sin validación.

## ✅ Impacto

- Acceso a servicios internos.
- Enumeración de APIs.
