#!/usr/bin/env python3
import requests
import sys

def main():
    try:
        response = requests.get('http://localhost:8000/api/ubicaciones/', timeout=5)
        if response.status_code == 200:
            datos = response.json()
            if datos:
                print("📍 Últimas ubicaciones registradas:")
                for u in datos:
                    print(f"- {u['usuario']}: lat {u['latitud']}, lon {u['longitud']} ({u['timestamp'][:16]})")
            else:
                print("No hay ubicaciones registradas aún.")
        elif response.status_code == 404:
            print("Error 404: Endpoint no encontrado", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"Error del servidor: {response.status_code}", file=sys.stderr)
            sys.exit(1)
    except requests.exceptions.ConnectionError:
        print("Error: No se pudo conectar con Django. ¿Está corriendo en puerto 8000?", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()