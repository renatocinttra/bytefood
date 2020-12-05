def init_app(app):
    app.config['SECRET_KEY'] = "mudar@123"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bytefood.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    if app.debug:
        app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True
        app.config['DEBUG_TB_PROFILER_ENABLED'] = True
