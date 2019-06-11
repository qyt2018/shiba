# coding: utf-8
from sanic import Sanic
from config import dev as config
from views import urlpatterns
from sanic_motor import BaseModel


def make_app():
    app = Sanic(__name__)
    app.config.from_object(config)
    app.static('/_nuxt', app.config['NUXT_STATIC_DIR'])
    for url in urlpatterns:
        app.add_route(url[1], url[0])

    BaseModel.init_app(app)
    return app


if __name__ == "__main__":
    app = make_app()
    app.run(app.config['HOST'], app.config['PORT'], app.config['DEBUG'])
