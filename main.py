from flask import Flask,jsonify, request,json

app=Flask(__name__)


desenvolvedores=[

{
    'id':'0',    
    'nome':'rafael',
    'habilidades':['python','java']
},

{
     'id':1,    
     'nome':'ude',
     'habilidades':['python','tkinter']
}

]


@app.route('/dev/<int:id>/',  methods=['GET', 'PUT','DELETE'])
def devs(id):
    if request.method == 'GET':
         desenvolvedor=desenvolvedores[id]
         print(desenvolvedor)
         return jsonify(desenvolvedor)
    elif request.method == 'PUT':
         dados=request.blueprint
         dados=json.loads(request.data)
         desenvolvedores[id]=dados
         return jsonify(dados)
    elif request.method == 'DELETE':
         desenvolvedores.pop(id)
         return jsonify({'status':'sucesso','msn':'registro excluido'})

@app.route('/dev/', methods=['POST','GET'])
def lista_desenvolvedores():
     if request.method == 'POST':
          dados=json.loads(request.data)
          posicao=len(desenvolvedores)
          dados['id']=posicao
          desenvolvedores.append(dados)
          return jsonify(desenvolvedores[posicao])
     
     elif request.method == 'GET':
          return jsonify(desenvolvedores)
         

if __name__=="__main__":
    app.run(debug=True)