def obtener_velocidad():
    """
    Solicita al usuario una velocidad y la valida.
    Devuelve un valor entero entre 0 y 255.
    """
    while True:
        user_velocity = input("Introduce una velocidad válida [entre 0,255]: ")    
        if user_velocity.isnumeric():
            user_velocity = int(user_velocity)
            if user_velocity <= 255:
                return user_velocity
            else:
                print("La velocidad no está en el rango permitido")
        else:
            print("Velocidad inválida")
