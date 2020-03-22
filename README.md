# YouWish
## Notas de instalación con Pipenv.

> Aclaración: Esta modalidad tiene ciertos pre requisitos:
>
> - Contar con python3
> - Contar con pip3
>
> Esto se puede hacer en cualquier SO.

Para ejecutar la aplicación en un browser se debe instalar pipenv mediante el comando:

```
pip install pipenv
```

Luego iniciar el entorno virtual con el comando:
```
pipenv shell
```

Finalmente con el siguiente quedan instaladas todos los modulos necesarios para la aplicacion.
```
pipenv install --ignore-pipfile
```

## Notas de desarrollo con Pipenv.

Para sistematizar el desarrollo de la aplicación y facilitar el flujo de trabajo, se utiliza pipenv como gestor de paquetes. 

https://pipenv-es.readthedocs.io/es/latest/

En general, instalar pipenv se puede lograr mediante el comando:

```
pip install pipenv
```

Para crear un entorno desde cero se debe ejecutar el comando (idem para iniciar un entorno ya creado):

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

## Notas de ejecución con Pipenv.

Ejecutar el siguiente comando para iniciar el entorno (si ya se esta ejecutando el entorno, entonces saltear el paso)

```
pipenv shell
```

Finalmente se ejecuta el comando en python

```
python app.py
```

y se abre un explorador en la dirección `localhost:4000`. Esto mismo se indica en la terminal al momento de ejecutar la aplicación.



## Notas de instalación con Docker.

Para asegurar la portabilidad de la aplicación y su desarrollo, se puede utilizar Docker. Los siguientes vídeos pueden ser de ayuda para entender que es docker, como instalarlo y usarlo.

- [¿Que es Docker?](https://www.youtube.com/watch?v=hQgvt-s-AHQ)
- [¿Como se instala (windows 10)?](https://www.youtube.com/watch?v=BK-C2RofmTE) 
- [¿Como se instala (ubuntu)?](https://www.youtube.com/watch?v=BK-C2RofmTE)
- [¿Como se uso para el desarrollo de la aplicacion?](https://www.youtube.com/watch?v=YENw-bNHZwg&t=1464s)

> Nota: En windows, instale docker junto con su compatibilidad con contenedores linux, ya que la mayoría de la aplicación fue desarrollada en ese entorno. Acorde a esto, debe hacer un switch al modo de compatibilidad con contenedores linux. Esto ultimo se puede hacer desde el sub menú de configuración de docker en la barra de tareas

En primer lugar, instalar Docker y asegurarse de que se este ejecutando (esto depende de su SO).

Luego ejecute el siguiente comando sobre la dirección de la carpeta donde haya colocado el código de la aplicación, para generar la imagen base.

```
docker build -t wpsapp .
```

Esto creara una imagen base llamada `wpsapp`. Tranquilamente puede tener cualquier otro nombre. Para asegurarse de que se creo correctamente, ejecute el comando `docker images`, que listara todas las imágenes creadas hasta el momento.

## Notas de ejecución con Docker

Ejecutar el siguiente comando (asegurarse de que Docker esta corriendo)

```
docker run -it -p 4000:4000 wpsapp
```

y la aplicación ya estará disponible en la dirección `localhost:4000`.