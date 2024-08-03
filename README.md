# Proyecto de Reconocimiento de Códigos de Barras mediante ESP32-CAM y Raspberry Pi
## Objetivo
Desarrollar un prototipo de sistema de seguridad integral de 
detección de códigos QR y visión por computadora para el 
control de accesos, la identificación y la prevención de delitos en 
industrias de seguridad, policiales y militares.

## Descripción del Proyecto

Este proyecto utiliza una cámara ESP32-CAM para capturar imágenes de códigos de barras y enviarlas a una Raspberry Pi, 
que utiliza la biblioteca OpenCV para procesar las imágenes y reconocer los códigos de barras. 
El proyecto también utiliza un socket para enviar los datos reconocidos desde la Raspberry Pi a un servidor.

## Objetivos del Proyecto

* Reconocer códigos de barras utilizando una cámara ESP32-CAM y la biblioteca OpenCV en una Raspberry Pi.
* Enviar los datos reconocidos desde la Raspberry Pi a un servidor mediante un socket.
* Desarrollar un sistema de reconocimiento de códigos de barras rápido y preciso.

## Componentes Utilizados


* **ESP32-CAM**: una cámara de alta resolución con capacidad de conexión Wi-Fi, utilizada para capturar imágenes de códigos de barras.
* **Raspberry Pi**: una computadora de placa única utilizada para procesar las imágenes y reconocer los códigos de barras.
* **OpenCV**: una biblioteca de visión por computadora utilizada para procesar las imágenes y reconocer los códigos de barras.
* **Socket**: un mecanismo de comunicación utilizado para enviar los datos reconocidos desde la Raspberry Pi a un servidor.


## Dependencias de Código

* El código en Arduino (ESP32-CAM) utiliza las bibliotecas `WebServer`, `WiFi` y `esp32cam`.
* El código en Python para la Raspberry Pi utiliza las bibliotecas `socket`, `OpenCV` y `pyzbar`.


## La biblioteca 
*socketen Python proporciona una interfaz para trabajar con sockets, que son puntos finales para la comunicación entre procesos en una red. La función principal de socketes:
*Crear conexiones de red :
*Enviar y recibir datos :

*OpenCV(Open Source Computer Vision Library) es una biblioteca de visión por computadora que proporciona funciones para procesar imágenes y videos. La función principal de OpenCVes:
*Procesar imágenes y vídeos : proporciona
*Realizar operaciones de visión por computadora : proporción
*Detección de bordes y cont
*Reconocimiento de patrones
*Segmento
*Reconocimiento facial y de objetos.

*pyzbares una biblioteca de código abierto que proporciona funciones para reconocer códigos de barras en imágenes. La función principal de pyzbares:
*Reconocer códigos de barras :
*Codigos
*Códigos de barras 2D (Código QR, Datos


## Notas
Recuerda que debes reemplazar las ip y puestos del codigo, como tanbien las contraseñas. 
.


Este proyecto fue realizado en el marco del curso IoT Essentials Developer impartido por [Codigo IoT ](https://www.codigoiot.com/) y organizado por la [Asociación Mexicana del Internet de las Cosas](https://www.asociacioniot.org/).