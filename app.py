from chalice import Chalice

app = Chalice(app_name="auth-microsservice")


@app.route("/")
def index():
    return {"hello": "world"}
