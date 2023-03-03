from flask import Blueprint

Maestros = Blueprint('Maestros', __name__)

@Maestros.route('/getmaes', methods=['GET'])
def getMaes():
    return {'key':'value'}