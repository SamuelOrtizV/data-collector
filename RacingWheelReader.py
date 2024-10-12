import pygame
import time
import sys
import logging
from typing import Tuple

class RacingWheelReader:
    """
    Lee el estado actual de un volante y sus pedales.
    """

    joystick: pygame.joystick
    name: str
    joystick_id: int

    def __init__(self, total_wait_secs: int = 10):
        """
        Inicializa el volante.
        
        - total_wait_secs: Número de segundos a esperar antes de comenzar a leer el estado del volante.
          Pygame tarda un tiempo en inicializarse, durante los primeros segundos se pueden obtener lecturas incorrectas.
          Se recomienda esperar algunos segundos antes de empezar a leer los datos.
        """
        pygame.init()
        pygame.joystick.init()
        try:
            # Intenta inicializar el volante conectando el primer dispositivo
            self.joystick = pygame.joystick.Joystick(0)
            self.joystick.init()
        except pygame.error:
            logging.warning(
                "No se encontró un volante. Asegúrate de que el volante esté conectado y sea reconocido por Windows."
            )
            sys.exit()

        # Obtiene el nombre y el ID del volante
        self.name = self.joystick.get_name()
        self.joystick_id = self.joystick.get_id()

        # Espera algunos segundos antes de comenzar a leer el volante
        for delay in range(int(total_wait_secs), 0, -1):
            print(
                f"Inicializando la lectura del volante, esperando {delay} segundos para evitar lecturas incorrectas...",
                end="\r",
            )
            time.sleep(1)

        print(f"Capturando entrada de: {self.name} (ID: {self.joystick_id})\n")

    def read(self) -> Tuple[str, str]:
        """
        Lee el estado actual del volante y sus pedales.

        Salida:
        - steering: Valor actual del eje X del volante, en el rango [-1, 1]
        - throttle_brake: Diferencia entre el valor del pedal del acelerador y el freno, en el rango [-1, 1]
        """
        pygame.event.pump()  # Actualiza el estado de los eventos del joystick
        steering = self.joystick.get_axis(0)  # Eje X del volante
        throttle = self.joystick.get_axis(1)  # Eje del pedal del acelerador
        brake = self.joystick.get_axis(2)     # Eje del pedal del freno

        # Normalizar los valores de los pedales para que estén en el rango [-1, 1]
        throttle_brake = (throttle - brake) / 2

        return f"{steering:.2f}", f"{throttle_brake:.2f}"

""" def imprimir_estado_volante() -> None:

    volante = RacingWheelReader()

    print("Leyendo el estado del volante (Ctrl+C para salir)...\n")

    try:
        while True:
            steering, throttle_brake = volante.read()  # Llama al método read
            print(f"Dirección: {steering}, Acelerar/Frenar: {throttle_brake}", end="\r")
            time.sleep(0.1)  # Pausa corta para evitar un loop muy rápido
    except KeyboardInterrupt:
        print("\nSaliendo...") """

# Ejecutar la función para leer el estado del volante
# if __name__ == "__main__":
#    imprimir_estado_volante()
