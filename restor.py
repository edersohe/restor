import tornado.ioloop
import tornado.web

class ResTorHandler(tornado.web.RequestHandler):
    def get(self, *args, _id=None, _new=None, _edit=None, **kwargs):
    	print(self.request.path)
    	print (_id, _new, _edit)

    	if not _id and not _new and not _edit:
    		self.index(*args, **kwargs)
    	elif _id and not _new and not _edit:
    		self.show(_id, *args, **kwargs)
    	elif not _id and not _edit and _new == 'new':
    		self.new(*args, **kwargs)
    	elif _id and not _new and _edit == 'edit':
    		self.edit(_id, *args, **kwargs)
    	else:
    		raise tornado.web.HTTPError(404)


    def post(self, *args, **kwargs):
    	self.create(*args, **kwargs)
    	
    def put(self, _id, *args, **kwargs):
    	if not _id:
    		raise tornado.web.HTTPError(404)
    	self.update(_id, *args, **kwargs)

    def delete(self, _id, *args, **kwargs):
    	if not _id:
    		raise tornado.web.HTTPError(404)
    	self.destroy(_id, *args, **kwargs)

    def index(self, *args, **kwargs):
    	print("index")
    	raise tornado.web.HTTPError(405)

    def new(self, *args, **kwargs):
    	print("new")
    	raise tornado.web.HTTPError(405)

    def create(self, *args, **kwargs):
    	print("create")
    	raise tornado.web.HTTPError(405)

    def show(self, _id, *args, **kwargs):
    	print("show", _id)
    	raise tornado.web.HTTPError(405)

    def edit(self, _id, *args, **kwargs):
    	print("edit", _id)
    	raise tornado.web.HTTPError(405)

    def update(self, _id, *args, **kwargs):
    	print("update", _id)
    	raise tornado.web.HTTPError(405)

    def destroy(self, _id, *args, **kwargs):
    	print("destroy", _id)
    	raise tornado.web.HTTPError(405)





application = tornado.web.Application([
    (r"/?(?:(?:(?P<_id>[0-9a-f]+)(?:/(?P<_edit>edit))?)|(?P<_new>new))?", ResTorHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()