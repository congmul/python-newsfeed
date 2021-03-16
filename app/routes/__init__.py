from .home import bp as home
from app.routes import home

@app.route('/hello')
def hello():
  return 'hello world'

# register routes
app.register_blueprint(home)

return app