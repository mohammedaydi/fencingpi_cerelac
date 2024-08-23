from flask import Blueprint
import controllers.purple_controllers as controllers

purple_bp = Blueprint('purple', __name__)


@purple_bp.get('/forward')
def move_forward():
    return controllers.move_forward()

@purple_bp.get('/backward')
def move_backwards():
    return controllers.move_backwards()

@purple_bp.get('/side')
def rotate_right():
    return controllers.rotate_right()

@purple_bp.route('/defend')
def rotate_left():
    return controllers.rotate_left()

@purple_bp.get('/high')
def hit():
    return controllers.high()

@purple_bp.get('/shield')
def shield():
    return controllers.shield()

@purple_bp.get('/purple/alive')
def is_alive():
    return controllers.is_alive()

@purple_bp.get('/purple/disconnect')
def disconnect():
    return controllers.disconnect()