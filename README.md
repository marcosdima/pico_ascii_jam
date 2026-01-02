# Pico ASCII Jam

Proyecto pygame con estructura modular para juego/aplicación.

## Estructura del Proyecto

```
pico_ascii_jam/
├── src/
│   ├── main.py          # Punto de entrada
│   ├── config.py        # Configuración global
│   ├── game.py          # Manejador principal del juego
│   └── scenes/
│       ├── __init__.py
│       └── menu.py      # Escena del menú
├── assets/              # Recursos (fuentes, imágenes, etc.)
└── requirements.txt     # Dependencias del proyecto
```

## Instalación

1. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

2. Para ejecutar el juego, desde el directorio raíz:
```bash
cd src
python main.py
```

## Configuración

Edita [src/config.py](src/config.py) para cambiar:
- Dimensiones de la ventana
- Colores
- FPS
- Rutas de recursos

## Fuente personalizada

Para usar una fuente personalizada:
1. Coloca un archivo `font.ttf` en la carpeta `assets/`
2. La aplicación usará automáticamente esta fuente si existe

Si no existe la fuente, se usará la fuente por defecto de pygame.

## Controles

- **ESC** o cerrar ventana: Salir del juego
