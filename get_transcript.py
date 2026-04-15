import os
import subprocess
import sys

def download(vid, name):
    try:
        # Creamos la carpeta
        os.makedirs("research/youtube-transcripts", exist_ok=True)
        path = f"research/youtube-transcripts/{name}.txt"
        
        print(f"⏳ Intentando descargar transcripción de {vid}...")
        
        # Llamamos a la herramienta directamente por fuera de Python
        cmd = [
            sys.executable, "-m", "youtube_transcript_api", 
            vid, "--format", "text"
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            with open(path, "w", encoding="utf-8") as f:
                f.write(result.stdout)
            print(f"✅ ¡POR FIN LO LOGRAMOS! Archivo '{name}.txt' creado.")
        else:
            print(f"❌ Error de la herramienta: {result.stderr}")
            
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

download("9bZkp7q19f0", "test-noticias")
