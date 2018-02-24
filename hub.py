import dinoWorld
import atlantis
import warWorld
import iceWorld
import future
import postApocWorld

def run(app):
    app.update_console('Choose a world to visit:')
    app.update_buttons([('Atlantis', lambda: atlantis.run(app)), ('Future', lambda: future.run(app)), ("Post-Apocalyptic World", lambda: postApocWorld.run(app))])