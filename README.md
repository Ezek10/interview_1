# Entrevista tecnica

## Descripción

Este repositorio esta preparado para la resolucion de la entrevista tecnica propuesta por ___ para un puesto como Software Support Engineer.
Se puede encontrar las condiciones de la entrevista en "Consigna.docx" (nota 1)

## Docker

Descarga la imagen

    docker pull ezemarcel/talana_app:latest

Ahora corre la imagen

    docker run --name talana --rm -p 8000:80 ezemarcel/talana_app

## Instalación

Clone el repositorio: 

    git clone https://github.com/Ezek10/interview_1.git

Cree una unidad virtual: 

    python -m venv .venv

Activar ambiente virtual:

    .\.venv\Scripts\activate

Instale las dependencias:

    pip install -r requirements.txt

## Uso

Para correr el programa corra:

    uvicorn src.app:app

o

    make run

y luego realice la siguiente request:

    curl --location 'localhost:8000/fight' \
    --header 'Content-Type: application/json' \
    --data '{
        "player1":
            {
                "movimientos": ["SDa", "DSD", "SA", "DSD"],
                "golpes":["K", "P", "K", "P"]
            }, 
        "player2":
            {
                "movimientos":["DSD", "WSA", "ASA", "", "ASA", "SA"],
                "golpes":["P", "K", "K", "K", "P", "k"]
            }
    } '


respuesta esperada:

    [
        "¡El combate comenzo! Tonyn Stallone dara el primer golpe",
        "Tonyn Stallone dio una gran patada",
        "Arnaldor Shuatseneguer dio un puñetazo",
        "Tonyn Stallone lo revento con un Taladoken",
        "Arnaldor Shuatseneguer lo revento con un Remuyuken",
        "Tonyn Stallone dio una gran patada",
        "Arnaldor Shuatseneguer lo revento con un Remuyuken",
        "Tonyn Stallone murio, sus familiares van a llorarlo toda su vida",
        "Arnaldor Shuatseneguer sobrevivio, y le quedo 1 energia"
    ]


## Debbug in VSCode

Copiar el siguiente codigo en .vscode/launch.json

    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Uvicorn run",
                "type": "python",
                "cwd": "${workspaceFolder}/",
                "request": "launch",
                "program": "${workspaceFolder}/.venv/Scripts/uvicorn.exe",
                "args": [
                    "src.app:app"
                ],
                "console": "integratedTerminal",
                "justMyCode": true
            }
        ]
    }

## Tests

Para correr los tests de esta aplicacion se recomienda usar el siguiente comando 

    pytest --cov --cov-config=.coveragerc --cov-report=html

o

    make test

puede abrir el archivo **htmlcov/index.html** para ver el coverage generado de los tests

## Cómo contribuir

Si bien este proyecto solo implica los conocimientos al momento de hacer esta entrevista creo que siempre puede ser bueno saber como se puede mejorar una entrega de este tipo, desde la funcionalidad del codigo, los tests hasta la documentacion o la presentacion del corriente archivo.

Si alguien se siente en capacidad de aportar sientase libre de crear una rama nueva y con un PR aportar sus ideas para mejorar esta presentacion

## Notas

- En la documentacion del ejercicio, el primer ejemplo aportado considere que tiene un error en el 3 comando de ataque del player 1, ya que menciona un ataque mientras que en los comandos no aporta ningun ataque

- Si bien hay algunas cosas que se podrian implementar no se hizo debido al alcance del ejercicio como Github Actions para realizar un Coverage Badge
