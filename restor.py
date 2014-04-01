import tornado.ioloop
import tornado.web
import traceback
import tornado.httputil


def action_routes(prefix, id_regex='[0-9a-f]+'):
    _id = "(?P<_id>%s)" % id_regex
    _arg1 = "(?:/(?P<_arg1>edit|delete))?"
    _arg2 = "(?P<_arg2>new)"
    route = "(?:/(?:(?:%s%s)|%s))?" % (_id, _arg1, _arg2)
    return r'' + prefix + route


class ActionsHandler(tornado.web.RequestHandler):
    def get(self, *args, _id=None, _arg1=None, _arg2=None, **kwargs):
        if not _id and not _arg2 and not _arg1:
            self.index(*args, **kwargs)
        elif _id and not _arg2 and not _arg1:
            self.show(_id, *args, **kwargs)
        elif not _id and not _arg1 and _arg2 == 'new':
            self.new(*args, **kwargs)
        elif _id and not _arg2 and _arg1 == 'edit':
            self.edit(_id, *args, **kwargs)
        else:
            raise tornado.web.HTTPError(404)

    def post(self, *args, _id=None, _arg1=None, _arg2=None, **kwargs):
        if not _id and not _arg1 and not _arg2:
            self.create(*args, **kwargs)
        elif _id and not _arg1 and not _arg2:
            self.update(_id, *args, **kwargs)
        elif _id and not _arg2 and _arg1 == 'delete':
            self.destroy(_id, *args, **kwargs)
        else:
            raise tornado.web.HTTPError(404)

    def put(self, *args, _id=None, _arg1=None, _arg2=None, **kwargs):
        if _id and not _arg1 and not _arg2:
            self.update(_id, *args, **kwargs)
        else:
            raise tornado.web.HTTPError(404)

    def delete(self, *args, _id=None, _arg1=None, _arg2=None, **kwargs):
        if _id and not _arg1 and not _arg2:
            self.destroy(_id, *args, **kwargs)
        else:
            raise tornado.web.HTTPError(404)

    def index(self, *args, **kwargs):
        self.write("Hola Mundo")
        # raise tornado.web.HTTPError(405)

    def new(self, *args, **kwargs):
        raise tornado.web.HTTPError(405)

    def create(self, *args, **kwargs):
        raise tornado.web.HTTPError(405)

    def show(self, _id, *args, **kwargs):
        raise tornado.web.HTTPError(405)

    def edit(self, _id, *args, **kwargs):
        raise tornado.web.HTTPError(405)

    def update(self, _id, *args, **kwargs):
        raise tornado.web.HTTPError(405)

    def destroy(self, _id, *args, **kwargs):
        raise tornado.web.HTTPError(405)


    def write_error(self, status_code, **kwargs):
        if "application/json" in self.request.headers.get("Accept", ""):
            self.set_header('Content-Type', 'application/json')
            response = {
                'error': True,
                'response': None,
                'code': status_code,
                'message': self._reason,
            }
            if self.settings.get("serve_traceback") and "exc_info" in kwargs:
                exc_info = traceback.format_exception(*kwargs["exc_info"])
                response['traceback'] = exc_info
            self.finish(response)
        else:
            super(ActionsHandler, self).write_error(status_code, **kwargs)


    def write(self, chunk):
        status_code = self.get_status()
        if status_code == 200 and \
                "application/json" in self.request.headers.get("Accept", ""):
            self.set_header('Content-Type', 'application/json')
            status_code = self.get_status()
            response = {
                'error': (status_code != 200 or None),
                'code': status_code,
                'message': tornado.httputil.responses[status_code], 
                'response': chunk
            }
            super(ActionsHandler, self).write(response)
        else:
            super(ActionsHandler, self).write(chunk)




application = tornado.web.Application([
    (action_routes('/animal'), ActionsHandler)
], debug=True)


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
