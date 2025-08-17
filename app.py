from astromoji.factory import create_app

app = create_app()

if __name__ == "__main__":
    # For local dev only; use `flask run` or a proper WSGI server in prod.
    app.run(debug=True)
