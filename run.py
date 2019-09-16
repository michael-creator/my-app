from app import app
app.init_app(app)

if __name__ == '__main__':
    app.run(debug = True)