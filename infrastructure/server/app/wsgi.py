from asgiref.wsgi import WsgiToAsgi
from infrastructure.server.app.application import init_app

app = WsgiToAsgi(init_app())

# if __name__ == "__main__":
#     app.run(host="0.0.0.0")
