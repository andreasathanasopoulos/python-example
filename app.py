from apistar import App, Route


def welcome(name=None):
    if name is None:
<<<<<<< HEAD
        return {"message": "Welcome to API Andreas!"}
    return {"message": "Welcome to API Andreas, %s!" % name}
=======
        return {"message": "Welcome to API Andreas!!"}
    return {"message": "Welcome to API Andreas, %s!\n" % name}
>>>>>>> 679a3a198d9301af285bbf18076256c23f717e0a


routes = [Route("/", method="GET", handler=welcome)]

app = App(routes=routes)


if __name__ == "__main__":
    app.serve("0.0.0.0", 5000, debug=True)
