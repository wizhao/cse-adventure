import dinoWorld
import atlantis
import warWorld
import iceWorld
import future
import postApocWorld

def run(app):
    app.change_location(("misc\\hub.png","A quiet, gateway world, open to various dimensions."))
    app.update_console('You arrive at the hub. Large arrays of portals swirl lazily.\n\nChoose a world to visit:\n')
    app.update_buttons([('Atlantis', lambda: atlantis.run(app)), ('Future', lambda: future.run(app)),
                        ("Post-Apocalyptic World", lambda: postApocWorld.run(app)),
                        ("Dino World", lambda: dinoWorld.run(app)), ('War World', lambda: warWorld.run(app)),
                        ('Ice World', lambda: iceWorld.run(app)), ('Storage', app.pull_out)])
