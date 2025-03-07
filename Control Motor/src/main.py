def main():
    """
    Función principal que muestra un mensaje de bienvenida y obtiene la velocidad del usuario.
    """
    welcome_message = """
    
            BIENVENIDOS AL SISTEMA MOTOR CONTROL
    Para comenzar, debes introducir una velocidad deseada:
    
    """
    print(welcome_message)
    velocidad = obtener_velocidad()
    print(f"Velocidad establecida: {velocidad}")

if __name__ == "__main__":
    main()