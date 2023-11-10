import flask
import flags
from api import rest_api

PORT = 9002

def main():
	app = flask.Flask(__name__)
	app.register_blueprint(rest_api)

	# Load server
	print(f"CodeMaze Flag Manager running on port {PORT}")
	app.run(host='0.0.0.0', port=PORT)


if __name__ == "__main__":
	main()