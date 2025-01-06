# README - Operaciones Modulares y Gráficas

Este proyecto implementa una serie de funciones para realizar operaciones modulares básicas y resolver ecuaciones modulares, además de graficar las clases de residuos. Además, incluye la capacidad de procesar entradas de datos manuales o desde un archivo CSV.

## Requisitos previos
Para ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.x**
- Librerías adicionales:
  - `math`
  - `csv`
  - `matplotlib`
  - `numpy`

Puedes instalar las dependencias faltantes usando `pip`:
```bash
pip install matplotlib numpy
```

## Archivos incluidos
- **`main.py`**: Contiene la lógica del programa, incluyendo las funciones para las operaciones modulares y la gráfica de residuos.

## Características principales
### 1. Operaciones Modulares Básicas
El programa soporta las siguientes operaciones modulares:
- **Suma Modular**: `(x + y) % n`
- **Resta Modular**: `(x - y) % n`
- **Multiplicación Modular**: `(x * y) % n`
- **Exponenciación Modular**: `(x^y) % n`

### 2. Ecuaciones Modulares Simples
Resuelve ecuaciones de la forma:
```
ax ≡ b (mod n)
```
utilizando el algoritmo de Euclides para encontrar el inverso modular.

### 3. Lectura de Archivos CSV
Permite procesar operaciones modulares desde un archivo CSV. Cada fila debe tener el siguiente formato:
```csv
x,operador,y,n
```
Donde:
- `x` y `y` son enteros,
- `operador` puede ser `+`, `-`, `*`, o `^`,
- `n` es el módulo.

### 4. Gráfica de Residuos Modulares
Representa las clases de residuos módulo `n` en un círculo utilizando `matplotlib`.

## Uso
### Ejecución del programa
Para ejecutar el programa:
```bash
python main.py
```

### Menú principal
Al iniciar, el programa ofrece dos opciones:
1. **Forma manual**: Introducir los valores manualmente.
2. **Archivo CSV**: Procesar las operaciones desde un archivo CSV.

#### Ejemplo de entrada manual:
```
Desea ingresar los valores o un archivo csv
1) Para forma manual
2) Para archivo csv
Opcion: 1
1) Operaciones modulares basicas
2) Ecuaciones modulares simples
Opcion: 1
El formato sera 'x operador y (mod n)'
x=5
operador=+
y=3
n=4
Resultado: 0
```

#### Ejemplo de archivo CSV:
Dado un archivo llamado `operaciones.csv` con el contenido:
```csv
x,operador,y,n
5,+,3,4
7,*,2,5
```
El programa generó un archivo actualizado con los resultados:
```csv
x,operador,y,n,Resultados
5,+,3,4,0
7,*,2,5,4
```

### Gráficas
Tras calcular una operación, el programa genera una gráfica de los residuos módulo `n` representados en un círculo.

## Estructura del código
### Funciones principales
- **`sumod(x, y, n)`**: Calcula la suma modular.
- **`resmod(x, y, n)`**: Calcula la resta modular.
- **`multiplicacion_modular(x, y, n)`**: Calcula la multiplicación modular.
- **`expmod(x, y, n)`**: Calcula la exponenciación modular.
- **`euclides(a, b)`**: Implementa el algoritmo de Euclides.
- **`ecuaciones(a, b, n)`**: Resuelve ecuaciones modulares simples.
- **`pedir_entero(mensaje)`**: Solicita un número entero al usuario con validación.
- **`mostrar_residuos_modulo(n)`**: Genera una gráfica circular de los residuos modulares.

## Manejo de errores
- Validación de entrada para asegurarse de que se introduzcan números enteros.
- Manejo de errores al leer archivos CSV (e.g., `FileNotFoundError`).

## Ejecución en sistemas Windows
Si deseas crear un ejecutable del programa para Windows, utiliza `PyInstaller`:
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```
El ejecutable se encontrará en la carpeta `dist/`.

## Licencia
Este proyecto se distribuye bajo la licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

