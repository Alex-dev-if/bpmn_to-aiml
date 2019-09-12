from flask import Flask, render_template, request, session

import aiml
import os
from random import *

app = Flask(__name__)
app.secret_key = 'any random string'

kernel = aiml.Kernel()
#kernel.learn("aiml/config.xml")
#kernel.respond("CEREBRO")
#kernel.loadSubs(filename = "aiml/substituicao.ini")

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "aiml/config.xml", commands = "CEREBRO")
    kernel.saveBrain("bot_brain.brn")

@app.route("/")
def home():
    sessionid = randint(1000,10000)
    session['sessionid'] = sessionid
    #print(sessionid)
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    usertext = request.args.get('msg')
    sessionid = session.get('sessionid')
    # print(sessionid)
    saida = kernel.respond(usertext, sessionid)
    if saida == '':
        saida = "Não entendi."
    return str(saida)


if __name__ == "__main__":
    app.run()