from nanobot import Agent
import requests
from datetime import datetime

# SKILL 1: Obtener ubicaciones
def obtener_ubicaciones():
    """
    Obtiene las últimas 10 ubicaciones registradas en el sistema.
    Útil cuando el usuario pregunta: '¿dónde está la gente?' o 'dame ubicaciones'
    """
    try:
        response = requests.get('http://localhost:8000/api/ubicaciones/', timeout=5)
        if response.status_code == 200:
            datos = response.json()
            if datos:
                resultado = "📍 Últimas ubicaciones registradas:\n"
                for u in datos:
                    resultado += f"- {u['usuario']}: lat {u['latitud']}, lon {u['longitud']} ({u['timestamp'][:16]})\n"
                return resultado
            return "No hay ubicaciones registradas aún."
        elif response.status_code == 404:
            return "Error 404: El endpoint no existe"
        else:
            return f"Error del servidor: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "Error: No se pudo conectar con el servidor. ¿Está Django corriendo?"
    except Exception as e:
        return f"Error inesperado: {str(e)}"

# SKILL 2: Registrar ubicación
def registrar_ubicacion(usuario: str, latitud: float, longitud: float):
    """
    Registra una nueva ubicación para un usuario específico.
    Útil cuando el usuario dice: 'registra mi ubicación en X, Y' o 'guarda que estoy en lat 10, lon 20'
    
    Parámetros:
    - usuario: nombre del usuario
    - latitud: coordenada de latitud
    - longitud: coordenada de longitud
    """
    try:
        data = {
            'usuario': usuario,
            'latitud': latitud,
            'longitud': longitud
        }
        response = requests.post('http://localhost:8000/api/ubicaciones/', 
                               json=data, timeout=5)
        if response.status_code == 201:
            return f"✅ Ubicación registrada exitosamente para {usuario}"
        elif response.status_code == 400:
            return f"Error: Datos inválidos. {response.json()}"
        else:
            return f"Error del servidor: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return "Error: No se pudo conectar con el servidor backend"
    except Exception as e:
        return f"Error al registrar: {str(e)}"

# Crear el agente
agente = Agent(
    name="Ubibot",
    system_prompt="""Eres un asistente que ayuda a gestionar ubicaciones.
    
    TIENES ESTAS HABILIDADES (SKILLS):
    1. obtener_ubicaciones() - Muestra las últimas ubicaciones guardadas
    2. registrar_ubicacion(usuario, latitud, longitud) - Guarda una ubicación
    
    Cuando un usuario pregunte por ubicaciones, USA obtener_ubicaciones().
    Cuando quiera guardar su ubicación, USA registrar_ubicacion().
    SIEMPRE usa las funciones disponibles, no inventes datos.
    Si hay errores de conexión, informa al usuario que el servidor no está disponible.
    """
)

# Registrar skills
agente.register_tool(obtener_ubicaciones)
agente.register_tool(registrar_ubicacion)

# Ejecutar
if __name__ == "__main__":
    print("🤖 Agente Ubibot iniciado (escribe 'salir' para terminar)\n")
    while True:
        user_input = input("👤 Tú: ")
        if user_input.lower() == 'salir':
            break
        respuesta = agente.run(user_input)
        print(f"🤖 Ubibot: {respuesta}\n")