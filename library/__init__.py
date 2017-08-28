from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')


#Routing the urls of the application
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include('.models')
    config.include('.routes')
    config.add_route('home', '/')
    config.add_route('hello', '/hello')
    config.add_route('new_book', '/new_book')
    config.add_route('browse', '/browse')
    config.scan()
    return config.make_wsgi_app()