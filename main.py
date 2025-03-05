import random
from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_human():
    return ("<h1>Hola Humano</h1>"
            "<p>En esta pagina hay varias cosas aleatorias</p>"
            "<a href=/Random>¡Ver un dato aleatorio!</a>"
            "<br></br>"
            "<a href=/coin>¡Tira una moneda!</a>"
            )

@app.route("/Random")
def Random_fact():
    facts_list = ["La dependencia a la technologia causa estress a las personas fuera de un area con covertura",
                  "Mas de 50% de las personas entre 16 y 30 años se consideran dependientes a la technologia",
                  "Una forma de combatir la dependencia a la technologia es buscar una actividad que mejore el estado de animo"
                  ]
    return (f"<p>{random.choice(facts_list)}</p>"
            "<a href=/Random>¡Ver otro dato aleatorio!</a>"
            "<br></br>"
            "<a href=/>Vuelta al inicio!</a>"
            )

@app.route("/coin")
def coin_flip():
    coin_toss = ["cara",
                  "cruz"
                  ]
    return (f"<p>{random.choice(coin_toss)}</p>"
            "<a href=/coin>¡Vuelve a tirar la moneda!</a>"
            "<br></br>"
            "<a href=/>Vuelta al inicio!</a>"
            )

app.run(debug=True)
