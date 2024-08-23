from flask import Blueprint
import controllers.cerelac_controllers as controllers


cerelac_bp = Blueprint('cerelac', __name__)

@cerelac_bp.route('/')
def home():
    return controllers.home()

@cerelac_bp.get('/health')
def get_health():
    return controllers.get_health()

@cerelac_bp.get('/available')
def checkAvailable():
    return controllers.checkAvailable()

@cerelac_bp.post('/auth')
def authenticate():
   return controllers.authenticate()

@cerelac_bp.post('/tmpauth')
def tmpauth():
    return controllers.tmpauth()

@cerelac_bp.get('/alive/states')
def alive_state():
    return controllers.alive_state()