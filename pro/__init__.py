from pro.bg.view import bg
def create_app(app):
    app.register_blueprint(bg,url_prefix='/bg')
