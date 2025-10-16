# 🤖 Proyecto Testing Automatización: Pre-Entrega 

<br>

## 🧭 Tabla de Contenidos

1.  [Propósito del Proyecto](#-propósito-del-proyecto)
2.  [Tecnologías Utilizadas](#-tecnologías-utilizadas)
3.  [Instrucciones de Instalación de Dependencias](#-instrucciones-de-instalación-de-dependencias)
4.  [Comando para Ejecutar Pruebas](#-comando-para-ejecutar-pruebas)

***

## 1. 🎯 Propósito del Proyecto

El objetivo principal de esta pre-entrega es **aplicar y consolidar los conocimientos adquiridos** hasta la Clase 8 del curso, demostrando la capacidad para automatizar flujos básicos de navegación web utilizando **Selenium WebDriver** y **Python**.

Este proyecto pone en práctica:
* La **interacción con elementos web** (clics, envío de texto).
* El uso de **estrategias de localización** (como `By.ID`, `By.XPATH`, etc.).
* La **validación de estados** mediante aserciones (Pytest).

El sitio objetivo para esta automatización es [Sauce Demo](https://www.saucedemo.com/), una aplicación web demo diseñada para prácticas de testing.

***

## 2. 💻 Tecnologías Utilizadas

| Herramienta | Función Principal |
| :--- | :--- |
| **Python** | Lenguaje de programación base. |
| **Selenium WebDriver** | Automatización de la interacción con el navegador. |
| **Pytest** | Framework para la estructura, ejecución y aserciones de los tests. |
| `pytest-html` | (Asumido) Para generar reportes profesionales en HTML. |
| `webdriver-manager` | (Recomendado) Para gestionar automáticamente el driver del navegador. |

***

## 3. 💾 Instrucciones de Instalación de Dependencias

Sigue estos pasos para obtener y configurar el proyecto:

###  Clonar el Proyecto

Abre tu terminal y utiliza el siguiente comando:

git clone https://github.com/vmstani/pre-entrega-automation-testing-Veronica-Stanislavsky.git

## 4. ▶️ Comando para Ejecutar Pruebas
Ejecuta el siguiente comando desde el directorio raíz para iniciar la automatización y generar un informe detallado.

pytest -v --html=reporte.html
