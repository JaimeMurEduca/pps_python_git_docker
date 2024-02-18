# Fase de resolución de dependencias
FROM python:slim AS builder

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar solo los archivos necesarios para instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Fase de ejecucion
FROM builder as runner

# Copiar el resto de los archivos de la aplicación
COPY . .

# Ejecutar tu aplicación
CMD ["python", "app.py"]
