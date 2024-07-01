from pro import create_app
from query import app
create_app(app)

if __name__ == '__main__':
    app.run(debug=True)