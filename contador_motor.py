import cv2
from ultralytics import YOLO
import os
from datetime import datetime

# Configuraciones
MODELO_PATH = 'yolov8n.pt'
CONFIDENCIA = 0.45

def guardar_reporte(ruta_video, conteo_maximo, promedio):
    """Genera el txt con los datos"""
    ruta_txt = os.path.splitext(ruta_video)[0] + ".txt"
    with open(ruta_txt, "w") as f:
        f.write(f"Fecha de analisis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Video original: {os.path.basename(ruta_video)}\n")
        f.write(f"Maximo personas vistas al tiempo: {conteo_maximo}\n")
        f.write(f"Promedio de ocupacion: {int(promedio)}\n")
    return ruta_txt

def procesar_video(ruta_entrada):
    """
    Toma un video, lo procesa con YOLOv8, guarda el resultado
    y retorna la ruta del video procesado y del reporte.
    """
    if not os.path.exists(ruta_entrada):
        return None, None

    # Definir nombre de salida (ej: video.mp4 -> video_DETECTADO.mp4)
    nombre_base = os.path.splitext(ruta_entrada)[0]
    ruta_salida = f"{nombre_base}_DETECTADO.mp4"

    print(f"[MOTOR] Cargando modelo YOLOv8 para procesar: {ruta_entrada}...")
    model = YOLO(MODELO_PATH)

    cap = cv2.VideoCapture(ruta_entrada)
    if not cap.isOpened():
        return None, None

    # Propiedades del video
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Configurar grabador (mp4v para compatibilidad)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(ruta_salida, fourcc, fps, (width, height))

    # Variables estadísticas
    max_personas = 0
    suma_personas = 0
    total_frames = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # --- Lógica Original de tu contador2.py ---
        results = model.predict(frame, conf=CONFIDENCIA, classes=0, verbose=False) # classes=0 es persona
        annotated_frame = results[0].plot()
        
        cantidad = len(results[0].boxes)
        
        # Actualizar estadísticas
        if cantidad > max_personas:
            max_personas = cantidad
        suma_personas += cantidad
        total_frames += 1

        # Dibujar etiqueta (Igual que en tu código original)
        cv2.rectangle(annotated_frame, (10, 10), (350, 70), (0, 0, 0), -1)
        cv2.putText(annotated_frame, f"Total: {cantidad}", (20, 55), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 255), 3)

        # Guardar en disco (Sin imshow)
        out.write(annotated_frame)
        # ------------------------------------------

    cap.release()
    out.release()
    print(f"[MOTOR] Procesamiento terminado: {ruta_salida}")

    # Generar el reporte TXT
    promedio = suma_personas / total_frames if total_frames > 0 else 0
    ruta_txt = guardar_reporte(ruta_salida, max_personas, promedio)

    return ruta_salida, ruta_txt