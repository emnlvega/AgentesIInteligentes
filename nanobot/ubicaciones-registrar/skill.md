---
name: registrar-ubicacion
description: Registra una nueva ubicación enviando datos a la API Django
---

# Registrar Ubicación

Esta skill envía datos al endpoint POST /api/ubicaciones/ del backend.

## Cuándo usar
- Cuando el usuario quiere guardar su ubicación actual
- Cuando proporciona coordenadas específicas para registrar

## Cómo usar
El script espera exactamente 3 argumentos: usuario, latitud, longitud
Ejemplo: `python registrar_ubicacion.py "Juan" 19.4326 -99.1332`

## Implementación
Ejecuta el script con los argumentos extraídos de la conversación.