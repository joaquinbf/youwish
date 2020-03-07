# YouWish

## Notas de desarrollo.

Para sistematizar el desarrollo de la aplicación y facilitar el flujo de trabajo, se utiliza pipenv como gestor de paquetes. 

https://pipenv-es.readthedocs.io/es/latest/

En general, instalar pipenv se puede lograr mediante el comando:

```
pip install pipenv
```

Para crear un entorno desde cero se debe ejecutar el comando:

```
pipenv shell
```

Esto genera un entorno virtual donde nada de lo que se instala quedara de forma permanente en el sistema en que se este ejecutando la aplicación.

Todos los paquetes que se quieran instalar y que sean necesarios para la aplicación en si, se deben instalar mediante el comando:

```
pipenv install <paquete>
```

Si por otro lado, se quiere instalar un modulo solo para el desarrollo, se puede hacer mediante el comando:

```
pipenv install <paquete> --dev
```

Entonces para instalar todos los módulos necesarios (tanto de la aplicación como de desarrollo), se debe ejecutar el comando 

```
pipenv install
```

El comando `pipenv lock` hace un registro de las versiones de los distintos módulos usados y los guarda en el archivo `Pipfile.lock`. Esta es una excelente practica para evitar problemas al momento de desplegar la aplicación. 

Entonces, si se desea instalar lo que se haya registrado en el archivo `Pipfile.lock` y no lo que se marca en el archivo `Pipfile` se debe ejecutar el comando:

```
pipenv install --ignore-pipfile
```

Para salir del entorno virtual, simplemente se debe ejecutar el comando `exit`