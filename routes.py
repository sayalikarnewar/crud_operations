from views import get, retrieve, add, update, delete

def routes(app):
    app.router.add_get("/", get)
    app.router.add_get("/retrieve/{user}", retrieve)
    app.router.add_get("/add/{user}", add)
    app.router.add_get("/update/{old_user},{new_user}" ,update)
    app.router.add_get("/delete/{user}", delete)