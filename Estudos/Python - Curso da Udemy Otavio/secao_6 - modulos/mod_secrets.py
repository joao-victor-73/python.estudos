# O módulo secrets gera númerows aleatórios seguros <-> Aula 297

# Da para gerar senhar aleatórias e de forma mais segura
# utilizando esse módulo, e a aula foi ensinado a maneira de fazer;

import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=12)))
# k -> vai ser o tamanho da senha ou do texto