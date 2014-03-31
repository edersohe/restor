import tornado.ioloop
import tornado.web

class ResTorHandler(tornado.web.RequestHandler):
    def get(self, *args, _id=None, _arg1=None, _arg2=None, **kwargs):
    	print(self.request.path)
    	print (_id, _arg1, _arg2)

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
    (r"/?(?:(?:(?P<_id>[0-9a-f]+)(?:/(?P<_arg1>edit|delete))?)|(?P<_arg2>new))?", ResTorHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()