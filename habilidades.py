
from flask_restful import Resource




lista_habilidades=[

'python',
'java',
'c#',
'flutter'

]

class Habilidades(Resource):
    def get(self):
        return lista_habilidades




