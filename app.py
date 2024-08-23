from flask import Flask
from flask_cors import CORS
from routes.cerelac import cerelac_bp
from routes.purple_cerelac import purple_bp
from routes.black_cerelac import black_bp
from mqtt_network.mqtt_cerelac import initialize_mqtt

app = Flask(__name__)
CORS(app)

#register the middlewares
app.register_blueprint(cerelac_bp)
app.register_blueprint(purple_bp)
app.register_blueprint(black_bp)

initialize_mqtt();

if __name__ == '__main__':
    app.run(host= '0.0.0.0',port = 5000)

