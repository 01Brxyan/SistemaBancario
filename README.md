**Autor**

Brayan Snehyder Castro Velandia

**Descripción**

Este es un programa sencillo de simulación bancaria.
Permite crear cuentas, depositar dinero, retirar dinero, solicitar créditos, pagar cuotas, cancelar cuentas y ver la información de cada cliente.
Funciona desde la consola mediante un menú de opciones y está pensado como práctica de programación modular en Python.

**Stack Tecnológico**

* Python, por su simplicidad y versatilidad.
* Visual Studio Code como entorno de desarrollo.
* Consola o terminal como interfaz de uso (interfaz de texto, no gráfica).

**Requerimientos**

* Tener instalada una versión reciente de Python 3.
* No requiere librerías externas adicionales.

Ejecución: Cómo usar el programa

Funciona tanto en Linux como en Windows.
Se ejecuta desde Visual Studio Code o directamente desde la consola.
Al iniciarlo, se muestra un menú con opciones numeradas para realizar las operaciones bancarias.
El usuario selecciona una opción escribiendo el número correspondiente.

**Estructura de Archivos**

El programa está dividido en varios archivos para mayor organización:

* operaciones.py: Contiene la lógica de las operaciones bancarias.
* corefiles.py: Gestiona el menú principal y conecta con operaciones.
* utilidades.py: Incluye funciones auxiliares para entradas y validaciones.
* menu.py: Se encarga de invocar el menú.
* main.py: Es el punto de entrada del programa.

**Librerías Externas**

No se usaron librerías externas, solamente las funciones básicas que ya vienen con Python.
