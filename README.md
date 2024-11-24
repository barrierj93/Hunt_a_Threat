
# Hunt a Threat 🎮

**Hunt a Threat** es un juego interactivo en la terminal donde los jugadores asumen el rol de analistas de ciberseguridad. Tu objetivo es identificar grupos de hackers basándote en las descripciones de sus tácticas y ataques. ¿Tienes lo que se necesita para cazar la amenaza y salvar el día?

---

## 📖 Cómo Jugar

1. **Inicio del Juego**:
   - Al iniciar el juego, aparecerá un banner ASCII con el título "GUESS THE THREAT".
   - El juego te presentará una descripción de un ataque cibernético relacionado con un grupo de hackers.

2. **Objetivo**:
   - Identifica el grupo responsable de entre 4 opciones.
   - Si seleccionas correctamente, ganas puntos. Si fallas, pierdes una vida.

3. **Vidas y Final del Juego**:
   - Comienzas con 3 vidas.
   - Perder todas las vidas termina el juego y mostrará un mensaje de "YOU'VE BEEN PWND".

4. **Opciones al Final**:
   - Puedes reiniciar el juego o salir después de perder todas tus vidas.

---

## 🛠️ Instalación y Ejecución en Local

Sigue estos pasos para descargar y ejecutar el juego en tu máquina:

### 1. Clonar el Repositorio
Abre tu terminal y clona el repositorio de GitHub:
```bash
git clone https://github.com/tu-usuario/hunt-a-threat.git
```
Cambia al directorio del proyecto:
```bash
cd hunt-a-threat
```

### 2. Instalar Dependencias
Asegúrate de que tienes **Python 3.7+** instalado en tu sistema.

No se requieren dependencias externas para este juego, ya que utiliza únicamente módulos estándar de Python.

### 3. Ejecutar el Juego
Ejecuta el archivo `hunt_a_threat.py` desde la terminal:
```bash
python hunt_a_threat.py
```

---

## 🧑‍💻 Cómo Funciona

El juego utiliza un conjunto de datos de grupos de hackers y sus descripciones para generar preguntas aleatorias. Aquí está el flujo principal del juego:

1. Se selecciona aleatoriamente un grupo de hackers como respuesta correcta.
2. El jugador recibe cuatro opciones (una correcta y tres incorrectas).
3. El jugador elige una opción ingresando un número del 1 al 4.
4. Si la elección es incorrecta, el jugador pierde una vida. Si es correcta, gana un punto.

---

## 📂 Estructura del Proyecto

```
hunt-a-threat/
│
├── hunt_a_threat.py    # Código principal del juego
├── hacker_groups_cleaned.csv  # Dataset con información de grupos hackers (opcional)
└── README.md           # Este archivo
```

---

## 🚀 Características del Juego

- **Descripción Narrativa**: Basada en datos reales de ciberseguridad.
- **Sistema de Vidas**: Pierde vidas al fallar respuestas.
- **Arte ASCII**: Para darle un toque retro al juego.
- **Preguntas Aleatorias**: Basadas en datos variados para mejorar la rejugabilidad.
- **Opción de Reinicio**: Comienza desde cero tras un "Game Over".

---

## 🏆 ¿Puedes Ganar?
¡Descubre cuántos grupos puedes identificar antes de quedarte sin vidas! Comparte tu puntuación y desafía a tus amigos.

---

¿Tienes sugerencias o mejoras? ¡Siéntete libre de contribuir! 🎉

---

## 📜 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE). Siéntete libre de usar, modificar y compartir.
