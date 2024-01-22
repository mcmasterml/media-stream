from flask import Flask, render_template
from utils import Database


def create_app():
    app = Flask(__name__)

    with app.app_context():
        db_instance = Database('app_interactions')
        db_instance.spawnAll()

    @app.route('/', methods=['GET'])
    def renderLoginPage():
        return render_template('login.html')

    @app.route('/login', methods=['POST'])
    def startSession():
        db_instance.startSession()  # TODO: fix
        return render_template('home.html')

    @app.route('/browse', methods=['POST'])
    def browse():
        db_instance.browse()
        # TODO: anything. currently doing nothing.
        return render_template('home.html')

    @app.route('/watch-show', methods=['POST'])
    def watchShow():
        db_instance.spawnShow()
        db_instance.watchShow()  # TODO: implement
        return render_template('home.html')

    @app.route('/watch-ad', methods=['POST'])
    def watchAd():
        db_instance.spawnAdvertisement()
        db_instance.watchAdvertisement()
        return render_template('home.html')

    @app.route('/logout', methods=['POST'])
    def logout():
        db_instance.endSession()
        return render_template('login.html')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
