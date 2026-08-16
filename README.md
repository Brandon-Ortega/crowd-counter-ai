# 👥 Crowd Counter AI - Sistema Inteligente de Conteo de Multitudes

## 📋 Descripción del Proyecto

**Crowd Counter AI** es una solución integral de visión por computadora que utiliza **YOLOv8** (detección de objetos en tiempo real) para analizar videos y contar automáticamente la cantidad de personas presentes en cada fotograma. 

El sistema combina:
- 🤖 **Inteligencia Artificial**: Modelo YOLOv8 preentrenado para detección de personas
- 🎥 **Procesamiento de Video**: Análisis fotograma a fotograma
- 📊 **Estadísticas Automáticas**: Conteo máximo, promedio y reportes detallados
- 🌐 **Interfaz Web**: Dashboard intuitivo construido con Flask
- 📁 **Gestión de Archivos**: Organización automática de videos originales y procesados

---

## ✨ Características Principales

✅ **Detección de Personas en Tiempo Real**
- Utiliza YOLOv8n (modelo nano optimizado para velocidad)
- Confianza ajustable (por defecto 45%)

✅ **Procesamiento Automático de Videos**
- Genera video anotado con detecciones visuales
- Caja delimitadora alrededor de cada persona detectada
- Contador visible en cada fotograma

✅ **Análisis Estadístico**
- Máximo de personas detectadas simultáneamente
- Promedio de ocupación/densidad
- Reportes guardados en formato TXT

✅ **Interfaz Web Intuitiva**
- Dashboard con dos columnas: pendientes y procesados
- Vista previa de videos en HTML5
- Carga de nuevos videos directamente desde el navegador
- Reportes anexados a cada resultado

✅ **Escalabilidad**
- Accesible en red local (configuración multi-dispositivo)
- Estructura modular y extensible
- Almacenamiento local de resultados

---

## 🛠️ Requisitos Previos

- **Python 3.8+**
- **OpenCV** (procesamiento de video)
- **YOLOv8** (detección de objetos)
- **Flask** (servidor web)
- **GPU recomendada** (NVIDIA CUDA para procesamiento más rápido)

---

## 📦 Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/Crowd-Counter-AI.git
cd Crowd-Counter-AI
```

### 2. Crear entorno virtual (recomendado)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install flask opencv-python ultralytics
```

### 4. Descargar modelo YOLOv8
El modelo `yolov8n.pt` se descargará automáticamente en la primera ejecución. Si prefieres descargarlo manualmente:
```bash
from ultralytics import YOLO
YOLO('yolov8n.pt')  # Descargar modelo
```

---

## 🚀 Uso

### Iniciar el servidor
```bash
python app.py
```

El servidor estará disponible en:
- **Local**: `http://localhost:5000`
- **Red Local**: `http://[tu-ip]:5000`

### Flujo de Trabajo

1. **Subir Video**: Usa el formulario en la interfaz para cargar un video MP4
2. **Procesar con IA**: Haz clic en "⚙️ Procesar con IA"
3. **Esperar Análisis**: El sistema procesará el video frame a frame
4. **Ver Resultados**: 
   - Video anotado con detecciones
   - Reportes con estadísticas
   - Historial en la pestaña "✅ Resultados Analizados"

---

## 📁 Estructura del Proyecto

```
Crowd-Counter-AI/
│
├── app.py                          # Servidor Flask principal
├── contador_motor.py               # Motor de procesamiento con YOLOv8
├── yolov8n.pt                      # Modelo de IA (descargado automáticamente)
│
├── static/
│   └── videos/                     # Almacenamiento de videos
│       ├── video_original.mp4      # Video crudo
│       ├── video_original_DETECTADO.mp4  # Video procesado
│       └── video_original_DETECTADO.txt  # Reporte de análisis
│
└── templates/
    └── interfaz.html               # Frontend - Dashboard web
```

---

## 🔧 Componentes Principales

### `app.py` - Servidor Flask
**Responsabilidades:**
- Gestionar rutas HTTP (`/`, `/procesar`, `/subir`)
- Servir la interfaz web
- Orquestar el flujo de procesamiento
- Manejo de archivos

**Rutas:**
- `GET /` - Página principal con galería
- `POST /subir` - Cargar video nuevo
- `GET /procesar/<nombre_video>` - Procesar video con IA

### `contador_motor.py` - Motor de Visión IA
**Responsabilidades:**
- Cargar modelo YOLOv8
- Procesar videos frame a frame
- Detectar personas (clase 0 en COCO dataset)
- Generar estadísticas
- Guardar videos anotados

**Funciones:**
- `procesar_video(ruta_entrada)` - Procesa un video y retorna ruta de salida y reporte
- `guardar_reporte(ruta_video, conteo_máximo, promedio)` - Genera archivo TXT con estadísticas

### `interfaz.html` - Dashboard Web
**Características:**
- Responsive design
- Dos columnas: pendientes vs. procesados
- Reproductor video HTML5
- Visualización de reportes
- Upload form integrado

---

## 📊 Ejemplo de Reporte

Cuando se procesa un video, se genera automáticamente un archivo `.txt`:

```
Fecha de analisis: 2024-12-19 14:30:45
Video original: reunion_oficina.mp4
Maximo personas vistas al tiempo: 12
Promedio de ocupacion: 7
```

---

## 🎯 Casos de Uso

✔️ **Análisis de Eventos**
- Conciertos, festivales, concentraciones

✔️ **Seguridad y Vigilancia**
- Monitoreo de aforo en establecimientos
- Análisis de densidad de multitudes

✔️ **Planificación Urbana**
- Estudios de flujo peatonal
- Análisis de capacidad en espacios públicos

✔️ **Investigación Académica**
- Estudios de comportamiento colectivo
- Análisis de patrones de movimiento

---

## ⚙️ Configuración Avanzada

### Ajustar Confianza de Detección

En `contador_motor.py`, modifica:
```python
CONFIDENCIA = 0.45  # Aumentar para menos falsos positivos (0.0-1.0)
```

### Cambiar Puerto del Servidor

En `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Cambiar puerto aquí
```

### Usar GPU para Procesamiento Más Rápido

```python
# En contador_motor.py
model = YOLO(MODELO_PATH)
model.to('cuda')  # Usar GPU NVIDIA
```

---

## 📈 Rendimiento

| Métrica | Valor |
|---------|-------|
| **Modelo** | YOLOv8n (nano - optimizado) |
| **Precisión** | ~80-90% en ambientes controlados |
| **FPS** | 30-60 fps (CPU), 120+ fps (GPU) |
| **Tamaño Modelo** | ~6.2 MB |

*Los valores varían según hardware, iluminación y complejidad del video*

---

## 🐛 Solución de Problemas

### "ModuleNotFoundError: No module named 'flask'"
```bash
pip install flask
```

### "No module named 'ultralytics'"
```bash
pip install ultralytics
```

### Video procesado muy lento
- Utiliza GPU (NVIDIA CUDA)
- Reduce resolución del video
- Aumenta el valor de CONFIDENCIA para menos procesamiento

### Puerto 5000 ya en uso
Cambia el puerto en `app.py` a otro disponible (ej: 5001, 8000, etc.)

---

## 📜 Licencia

Este proyecto utiliza:
- **YOLOv8** bajo licencia AGPL/Comercial (Ultralytics)
- **Flask** bajo licencia BSD
- **OpenCV** bajo licencia Apache 2.0

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📧 Contacto y Soporte

Para reportar problemas, sugerencias o preguntas:
- Abre un **Issue** en GitHub
- Contacta al desarrollador

---

## 🔮 Futuras Mejoras

- [ ] Procesamiento en tiempo real con cámaras USB/IP
- [ ] Análisis de trayectorias y flujos
- [ ] Almacenamiento en base de datos
- [ ] Exportación de reportes a PDF/Excel
- [ ] Detección de objetos adicionales (vehículos, mochilas, etc.)
- [ ] Dashboard con gráficos estadísticos
- [ ] API REST para integración con otros sistemas
- [ ] Soporte para múltiples GPU
- [ ] Dockerización del proyecto

---

## 📚 Referencias y Recursos

- [YOLOv8 Documentación](https://docs.ultralytics.com/)
- [Flask Oficial](https://flask.palletsprojects.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [COCO Dataset](https://cocodataset.org/)

---

## 👨‍💻 Autor

**Desarrollador**: [Brandon Ortega]  
**Año**: 2025  
**Versión**: 1.0.0

---

<div align="center">

### ⭐ Si te fue útil, considera dar una estrella al proyecto ⭐

Hecho con ❤️ usando Python, YOLOv8 y Flask

</div>
