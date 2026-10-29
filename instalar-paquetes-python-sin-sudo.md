# Instalar paquetes de Python sin permisos de administrador (sudo)

Guía para los equipos del aula (Ubuntu 24.04, Python 3.12), probada instalando `mysql-connector-python`.

## El problema

Al intentar instalar un paquete con pip directamente:

```bash
pip install mysql-connector-python
```

aparece este error:

```
error: externally-managed-environment
```

Desde Python 3.12, Ubuntu/Debian protege el Python del sistema (norma PEP 668) y no permite instalar paquetes con `pip` fuera de un entorno virtual.

La solución habitual (`python3 -m venv`) tampoco funciona en estos equipos, porque falta el paquete `python3.12-venv` y para instalarlo hace falta `sudo`:

```
The virtual environment was not created successfully because ensurepip is not available.
```

## La solución: entorno virtual sin pip + get-pip.py

Se crea el entorno virtual **sin pip** y luego se instala pip dentro de él descargándolo con el script oficial `get-pip.py`. Todo queda en la carpeta personal del usuario, así que no hace falta `sudo`.

```bash
rm -rf ~/venv-mysql                                   # borra un intento anterior fallido, si lo hay
python3 -m venv --without-pip ~/venv-mysql            # crea el entorno sin pip
source ~/venv-mysql/bin/activate                      # activa el entorno
curl -sS https://bootstrap.pypa.io/get-pip.py | python   # instala pip dentro del entorno
pip install mysql-connector-python                    # instala el paquete
```

## Comprobación

```bash
which pip
# /home/<usuario>/venv-mysql/bin/pip

python -c "import mysql.connector; print(mysql.connector.__version__)"
# 26.7.0
```

## Uso en el día a día

- **Activar el entorno** en cada terminal nueva:
  ```bash
  source ~/venv-mysql/bin/activate
  ```
  Cuando está activo, el prompt empieza por `(venv-mysql)`.
- **Desactivarlo:** `deactivate`
- **Ejecutar un script sin activar el entorno:**
  ```bash
  ~/venv-mysql/bin/python mi_script.py
  ```
- **En un IDE** (VS Code, Thonny…), seleccionar como intérprete `~/venv-mysql/bin/python`.
- **Instalar más paquetes:** con el entorno activo, `pip install <paquete>` normalmente.

## Usar el entorno en VS Code

VS Code (extensión de Python) ofrece crear entornos con **Quick Create** o desde el gestor **venv** (botón `+`). **No usar esas opciones**: internamente ejecutan `python3 -m venv`, que falla en estos equipos por la misma falta de `ensurepip`. Lo que hay que hacer es indicarle el entorno ya creado:

1. Si se abrió algún menú de creación de entorno, cerrarlo con **Esc**.
2. Pulsar **Ctrl+Shift+P** y elegir **Python: Select Interpreter** (o, en el panel de Python, el selector de entorno del proyecto).
3. Elegir **Enter Interpreter Path…** y escribir:
   ```
   /home/<usuario>/venv-mysql/bin/python
   ```
   Si se abre un explorador de archivos, navegar a la carpeta personal → `venv-mysql` → `bin` → `python`.
4. Comprobar que el proyecto muestra **venv-mysql (3.12.3)** y que dentro aparecen `mysql-connector-python` y `pip`.

A partir de ahí, los scripts ejecutados desde VS Code (botón *Run* o F5) usan ese entorno. La terminal integrada normalmente lo activa sola; si no, ejecutar `source ~/venv-mysql/bin/activate` en ella.

Si un intento fallido de creación dejó una carpeta `.venv` incompleta dentro del proyecto, se puede borrar.

## Prueba de conexión a MySQL

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="usuario", password="clave", database="mi_bd"
)
cur = conn.cursor()
cur.execute("SELECT VERSION()")
print(cur.fetchone())
conn.close()
```
