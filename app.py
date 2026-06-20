from flask import Flask, render_template, request, redirect, url_for
import os
import contador_motor  # <--- IMPORTAMOS TU CÓDIGO MODIFICADO

app = Flask(__name__)

# Configuración de carpetas
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
VIDEO_FOLDER = os.path.join(BASE_DIR, 'static', 'videos')

# Crear carpeta si no existe
if not os.path.exists(VIDEO_FOLDER):
    os.makedirs(VIDEO_FOLDER)

def obtener_info_txt(ruta_video_procesado):
    """Lee el txt asociado al video procesado si existe"""
    ruta_txt = os.path.splitext(ruta_video_procesado)[0] + ".txt"
    contenido = "Sin reporte"
    if os.path.exists(ruta_txt):
        with open(ruta_txt, 'r') as f:
            contenido = f.read()
    return contenido

@app.route('/')
def index():
    """Muestra la galería de videos (originales y procesados)"""
    archivos = os.listdir(VIDEO_FOLDER)
    videos_originales = []
    videos_procesados = []

    for archivo in archivos:
        if archivo.endswith(".mp4"):
            # Separamos los procesados de los originales
            if "_DETECTADO" in archivo:
                # Es un video ya procesado, buscamos su reporte
                ruta_completa = os.path.join(VIDEO_FOLDER, archivo)
                reporte = obtener_info_txt(ruta_completa)
                videos_procesados.append({'nombre': archivo, 'reporte': reporte})
            else:
                # Es un video crudo (original)
                videos_originales.append(archivo)

    return render_template('interfaz.html', originales=videos_originales, procesados=videos_procesados)

@app.route('/procesar/<nombre_video>')
def procesar(nombre_video):
    """Ruta que ejecuta la IA cuando el usuario lo pide"""
    ruta_video_entrada = os.path.join(VIDEO_FOLDER, nombre_video)
    
    print(f"[WEB] Solicitud de procesamiento para: {nombre_video}")
    
    # --- AQUÍ LLAMAMOS A TU CÓDIGO ---
    contador_motor.procesar_video(ruta_video_entrada)
    # ---------------------------------
    
    return redirect(url_for('index'))

@app.route('/subir', methods=['POST'])
def subir_video():
    """Permite subir videos nuevos desde el navegador"""
    if 'archivo' not in request.files:
        return redirect(url_for('index'))
    file = request.files['archivo']
    if file.filename == '':
        return redirect(url_for('index'))
    if file:
        file.save(os.path.join(VIDEO_FOLDER, file.filename))
        return redirect(url_for('index'))

if __name__ == '__main__':
    # host='0.0.0.0' para que sea accesible en tu red local
    app.run(debug=True, host='0.0.0.0', port=5000)