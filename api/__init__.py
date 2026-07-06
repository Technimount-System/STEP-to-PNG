from .steps import steps_bp

def register_blueprints(app):
    app.register_blueprint(steps_bp, url_prefix="/steps")