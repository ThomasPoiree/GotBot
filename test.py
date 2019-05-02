from flask import Flask, request , jsonify 
import numpy as np
import requests
import anapioficeandfire 


app = Flask(__name__) 
port = '5000' 
api = anapioficeandfire.API()



@app.route("/",methods=['POST']) 
def index():
	
	
	n = np.random.randint(1000)
	
	char = api.get_character(id=n) 
	  
		
	att = vars(char) 

	res = "Here are some infos about a random character ! \n" 
	LIST = ["books", "povBooks", "tvSeries","api","url"] 
	for v in att.keys() : 
		if str(v) == "allegiances" : 
			for id_ in att[v] : 
				id2 = "" 
				i = len(id_) -1 
				tmp = ""
				while id_[i] != "/" : 
					id2 = str(id_[i]) + id2
					i = i-1
				house = api.get_house(id=id2)
				tmp+= house.name + ' ,' 
				res += "allegiances : " + tmp[:-1] + "\n"	
		
		elif str(v) == "spouse" : 
			if att[v] != "" : 
				char = requests.get(att[v]) 
				res +="spouce : " +char.json()["name"] +"\n"	
		
		elif att[v] != "" and str(v) not in LIST  :

			
			X = att[v] 
			if type(X) == list : 
				if att[v] != [] :
					if att[v][0] != "" : 
						tmp = "" 
						for el in X : 
							tmp+= el + " , "

						res += str(v) + " : " + tmp[:-2] +"\n"
			else : 
				res += str(v) + " : " + att[v] + "\n" 

		else : 
			pass 

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

app.run(port=port)


