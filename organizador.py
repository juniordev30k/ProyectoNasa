import os, shutil
# Automatiza mover archivos .html y .css a una carpeta
if not os.path.exists('Web'):
    os.makedirs('Web')
for f in os.listdir('.'):
    if f.endswith(('.html', '.css')):
        shutil.move(f, f"Web/{f}")
        print(f"Automatizado: {f} movido a carpeta Web")
