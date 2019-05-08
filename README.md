# TC3041-P4-Primavera-2019

## 1. Descripción del problema

En este documento debe incluir el plantemaiento del problema diseñado así como la descripción de las mediciones, series, valores y etiquetas identificados en el problema.

Se requería guardar la información de 2 sensores importantes para el monitoreo de la salud de un paciente:

  1. Bomba de insulina
  
  2. Reloj inteligente

De la bomba de insulina se registran los niveles de azúcar en la sangre del paciente.

Del reloj inteligente se registran los siguientes datos:

  1. Ritmo cardiaco 
  
  2. Pasos realizados 
  
  3. Calorías quemadas
  
  4. Calorías ingeridas
  
  ## 2. Ejecución del programa
  
  1. Crear el contenedor de influxDB 

  `docker run --name influxDB -p 8086:8086 -d -v /var/lib/influxdb influxdb`

  2. Crear contenedor Grafana

  `docker run --name grafana -d -p 3000:3000 -v grafana:/var/lib/grafana grafana/grafana`
  
  3. Ejecutar el archivo "generarDatos.py" usando el comando
  
  `python generarDatos.py`
  
  4. Ingresa al navegador para hacer las graficas y ver los datos en Grafana
  
  `http://localhost:3000`
  
  5. Ingresa usuario y contraseña para entrar
  
  `usuario: admin`
  
  `contraseña: admin`

  
  **Para poder ejecutar el programa y generar los datos es importante instalar InfluxDB y Numpy
  
  ## 3. Resultado
  
    ![alt text](https://github.com/tec-csf/TC3041-P4-Primavera-2019-equipo-5/blob/master/dashboard.png)
    
 
 ## 4. Referencias
 
 * [InfluxDB en Python](https://www.influxdata.com/blog/getting-started-python-influxdb/)

## 5. Integrantes
1. [Joan Andoni González Rioz](https://github.com/JoanAndoni)
2. [Alejandra Tubilla Castellanos](https://github.com/alejandratub)
