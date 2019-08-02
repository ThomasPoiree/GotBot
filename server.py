from flask import Flask, request , jsonify 
import numpy as np
import requests
import os
import anapioficeandfire 
from bs4 import BeautifulSoup

app = Flask(__name__) 
port = int(os.environ["PORT"]) 
print(port)
 
api = anapioficeandfire.API()



@app.route("/",methods=['POST']) 
def index():
    

    
    requete = requests.get("https://jmentape.fr/")
    page = requete.content
    soup = BeautifulSoup(page, “html.parser”)
    txt = str(soup.find(“h1")).replace(‘<h1>‘, ‘’).replace(‘</h1>‘, ‘’)
    res = txt 
    return jsonify(

        status=200,
            replies=[{
              'type': 'text',
              'content': res
            }]
        )


@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port,host="0.0.0.0")


