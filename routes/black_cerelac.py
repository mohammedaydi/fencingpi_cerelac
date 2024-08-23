from flask import Blueprint
import controllers.black_controllers as controllers

black_bp = Blueprint('black', __name__)

@black_bp.get('/forward2')
def move_forward():
    return controllers.move_forward2()

@black_bp.get('/backward2')
def move_backwards():
    return controllers.move_backwards2()

@black_bp.get('/side2')
def rotate_right():
    return controllers.rotate_right2()

@black_bp.route('/defend2')
def rotate_left():
    return controllers.rotate_left2()

@black_bp.get('/high2')
def hit():
    return controllers.high2()

@black_bp.get('/shield2')
def shield():
    return controllers.shield2()

@black_bp.get('/black/alive')
def is_alive():
    return controllers.is_alive()


@black_bp.get('/black/disconnect')
def disconnect():
    return controllers.disconnect()