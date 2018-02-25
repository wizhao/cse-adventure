import dinoWorld
import atlantis
import warWorld
import iceWorld
import future
import postApocWorld
import winsound

def run(app):
    winsound.PlaySound('assets\\sounds\\portal.wav', winsound.SND_FILENAME)
    app.update_console('Choose a world to visit:')
    app.update_buttons([('Atlantis', lambda: atlantis.run(app)), ('Future', lambda: future.run(app)),
                        ("Post-Apocalyptic World", lambda: postApocWorld.run(app)),
                        ("Dino World", lambda: dinoWorld.run(app)), ('War World', lambda: warWorld.run(app)),
                        ('Ice World', lambda: iceWorld.run(app)), ('Storage', app.pull_out)])
