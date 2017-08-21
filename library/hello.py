from pyramid.view import view_config


@view_config(route_name='hello', renderer="templates/helloworld.mako")
def my_view(request):
    print("test")
    return {'project': 'library'}