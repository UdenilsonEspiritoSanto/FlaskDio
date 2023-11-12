from flask import Flask
from flask_restful import Resource, Api, request
import json
from habilidades import Habilidades

app=Flask(__name__)
api=Api(app)

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
class Desenvolvedores(Resource):
    def get(self,id):
       try:
           response = desenvolvedores[id]
       except IndexError:
          mensagem = 'Desenvolvedores de ID {} nao existe'.format(id)
          response = {'status':'erro','mensagem':mensagem}
       except Exception:
          mensagem = 'Erro desconhecido.procure o adm'
          response = {'status':'erro','mensagem':mensagem}
       return response
       
    def put(self,id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados
      
      
    def delete(self,id):
        desenvolvedores.pop(id)
        return ({'status':'sucesso','msn':'registro excluido'})
class Lista_Desenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados=json.loads(request.data)
        posicao=len(desenvolvedores)
        dados['id']=posicao
        desenvolvedores.append(dados)
        return (desenvolvedores[posicao])
    
api.add_resource(Lista_Desenvolvedores,'/dev/')   
api.add_resource(Desenvolvedores, '/dev/<int:id>/')
api.add_resource(Habilidades, '/habilidades/')

if __name__=='__main__':
    app.run(debug=True)
