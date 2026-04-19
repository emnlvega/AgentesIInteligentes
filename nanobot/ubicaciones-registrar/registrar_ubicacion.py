#!/usr/bin/env python3
import requests
import sys
import json

def main():
    if len(sys.argv) != 4:
        print("Error: Se requieren 3 argumentos: usuario latitud longitud", file=sys.stderr)
        print(f"Ejemplo: python {sys.argv[0]} Juan 19.4326 -99.1332", file=sys.stderr)
        sys.exit(1)
    
    usuario = sys.argv[1]
    try:
        latitud = float(sys.argv[2])
        longitud = float(sys.argv[3])
    except ValueError:
        print("Error: Latitud y longitud deben ser números", file=sys.stderr)
        sys.exit(1)
    
    try:
        data = {
            'usuario': usuario,
            'latitud': latitud,
            'longitud': longitud
        }
        response = requests.post('http://localhost:8000/api/ubicaciones/', 
                               json=data, timeout=5)
        if response.status_code == 201:
            print(f"✅ Ubicación registrada exitosamente para {usuario}")
        elif response.status_code == 400:
            print(f"Error: Datos inválidos - {response.json()}", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"Error del servidor: {response.status_code}", file=sys.stderr)
            sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con Django. ¿Está corriendo?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()