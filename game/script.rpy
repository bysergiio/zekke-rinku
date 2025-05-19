# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define z = Character("Zekke")
define p = Character("Cliente")
define m = Character("Mafioso")

image fondo pizza: 
    "pizzeria.png" 
    zoom 1.3
image fondo calle:
    "calle.png"
    zoom 1.3
image callejon:
    "callejon.png"
    zoom 1.3
image fondo calle2:
    "calle2.png"
    zoom 1.3
image puerta:
    "puerta.png"
    zoom 1.3
   
image pelea:
    "pelea.png"
    zoom 1.3

image zekkelibreta = "zekkelibreta.png"
image zekkemoto = "zekkemoto.png"
image zekkemotoenfadada:
    "zekkemotoenfadada.png"
    zoom 1.3
image zekkepuerta = "zekkepizza.png"
image mafioso = "mafioso.png"


label start:

    scene fondo pizza

    show zekkelibreta

    z "¡Hola! Buenas noches ¿en qué puedo ayudarle?"

    p "¡Hola! Quería pedir unas pizzas a domicilio."

    hide zekkelibreta

    "Tras hablar sobre los detalles del pedido, y con la pizza ya hecha, Zekke se ha preparado y ha salido a la calle."

label calle:

    scene fondo calle
    
    show zekkemoto 

    z "Llegamos tarde Byte, ¿qué hacemos?"

    menu:
        "Seguir por aquí.":
            jump calle2
        "Callejear":
            jump callejon

label calle2:

    show fondo calle2

    show zekkemoto

    z "Menos mal que hay poco tráfico, vamos a llegar ya mismo."

    hide zekkemoto

    "Con suerte a partir de ahí todos los semáforos estaban en verde, tardando menos de lo que se pensaba."

    menu:
        "Llegar al domicilio.":
            jump puerta

label callejon:

    show callejon

    "Zekke ha entrado en el callejón."

    show mafioso

    m "¡Seguidme! Juro haberla visto entrando por aquí."

    hide mafioso

    show zekkemotoenfadada

    z "Me están buscando, ¿ahora qué hago? Tengo que entregar la pizza."

    menu:
        "Salir corriendo.":
            jump puerta
        "Pelear":
            jump pelea 

label pelea:

    show pelea
    "Zekke ha peleado con los mafiosos. Con suerte, ha podido dejarlos atrás y ha llegado al domicilio para entregar la pizza."


label puerta:

    show puerta

    "Zekke ha llamado al timbre. La puerta se ha abierto."

    show zekkepuerta

    z "¡Buenas noches! Aquí está su pizza."

    # Finaliza el juego:
