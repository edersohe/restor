### Rest Handler based on actions prefix 

| url                 | method | action | html5 | form |
|:--------------------|:-------|:-------|:-----:|:----:|
| {prefix}            | GET    | index  | X     |      |
| {prefix}/:id        | GET    | show   | X     |      |
| {prefix}/:id/edit   | GET    | edit   | X     | X    |
| {prefix}/new        | GET    | new    | X     | X    |
| {prefix}            | POST   | create | X     |      |
| {prefix}/:id        | POST   | update | X     |      |
| {prefix}/:id        | PUT    | update |       |      |
| {prefix}/:id/delete | POST   | delete | X     |      |
| {prefix}/:id        | DELETE | delete |       |      |

> {prefix} should be "/animal", "/person", "/job" or any prefix that describe your route 

### Example

```python
import restor
import tornado.web

class MyActions(restor.ActionsHandler):

    def index(self):
        self.write("INDEX")

    def create(self):
        self.write("CREATE")

    def show(self, _id):
        self.write("SHOW " + _id)

    def update(self, _id):
        self.write("UPDATE " + _id)


application = tornado.web.Application([
    (restor.action_routes('/example'), MyActions)
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

```

* http://localhost:8888/example method GET  execute index action
* http://localhost:8888/example method POST execute create action
* http://localhost:8888/example/123 method GET execute show action with id 123
* http://localhost:8888/example/123 method UPDATE execute update action with id 123
* http://localhost:8888/example/123 method POST execute update action with id 123