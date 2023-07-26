from flask import Flask
from flask_cors import CORS
from leaderboard import leaderboard_bp


rsl_api = Flask(__name__)
cors = CORS(rsl_api)


# Register the endpoint blueprints
rsl_api.register_blueprint(leaderboard_bp, url_prefix='/api')


if __name__ == "__main__":
    rsl_api.run()