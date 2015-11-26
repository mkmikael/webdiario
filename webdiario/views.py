from pyramid.view import view_config

from webdiario.service import parse_rest

@view_config(route_name='home', renderer='templates/home.jinja2')
def my_view(request):
    return {'project': 'webdiario'}

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {'project': 'webdiario'}

@view_config(route_name='query', renderer='templates/_result.jinja2')
def query(request):
    if request.params['nome']:
        result = parse_rest.query(request.params['nome'])
    else:
        result = "Deu Merda"
    return {'result': result}