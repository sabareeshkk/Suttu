from werkzeug.exceptions import HTTPException
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule

from .app import App
from .globals import _request_var
from .Exceptions import InvalidArgumentException


class Suttu(App):
    """
    Initial entry point of the application
    """

    def __init__(self):
        # TODO:  make it accept __name__ for static and other files serving
        self.routes = {}
        self.url_map = Map()
        self.urls = None
        super().__init__()

    def route(self, path, methods=None, endpoint=None):
        """ add routes """
        if path is None:
            raise InvalidArgumentException
        # TODO: make decorator for routes
        if methods is None:
            methods = ["GET", "POST", "PUT", "DELETE"]
        if endpoint is None:
            endpoint = path

        def decorator(func):
            # TODO: add exception if func is no callable
            self.routes[endpoint] = func
            self.add_rule(path, endpoint, methods)
            return func

        return decorator

    def add_rule(self, path, endpoint, methods):
        """
        add routing Rules
        :param methods: request methods ['GET']
        :param path: url path
        :param endpoint: endpoint
        :return: None
        """
        rule = Rule(path, endpoint = endpoint, methods=methods)
        return self.url_map.add(rule)

    def dispatch_request(self, urls):
        try:
            endpoint, args = urls.match()
            view = self.routes[endpoint]
            result = view()
            return Response(result)
        except HTTPException as e:
            return Response(e.name, status=e.code)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        _request_var.set(request)
        urls = self.url_map.bind_to_environ(environ)
        response = self.dispatch_request(urls)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        """
        WSGI server calls the Suttu application object
        :param environ:
        :param start_response:
        :return:
        """
        return self.wsgi_app(environ, start_response)




