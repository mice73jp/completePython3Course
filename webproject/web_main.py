import web

urls = (
    '/(.*)/(.*)', 'index'
)

app = web.application(urls, globals())
render = web.template.render("resources/")

class index:

    def GET(self, name, age):
        # debug message
        # print("Hello ", name, ". How are you today?")
        # http://localhost:8080/NAME
        # http://localhost:8080/Chae MinSeok
        # return "<h1>Hello " + name + ".</h1> How are you today?"
        return render.main(name, age)


if __name__ == "__main__":
    app.run()
