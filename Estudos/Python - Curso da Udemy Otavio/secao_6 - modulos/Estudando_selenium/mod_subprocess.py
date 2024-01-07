import subprocess
import sys

# Verifica a plataforma que está
print(sys.platform)  # Saída -> win32

# Para exemplo, vamos utilizar o comando ping 127.0.0.1;
cmd = ['ping', '127.0.0.1']

subprocess.run(
    cmd,
    text=True,
    encoding='cp850'
)
