from routes import *
from sanic import Sanic
from sanic_cors import CORS
from tortoise.contrib.sanic import register_tortoise
import os

app = Sanic.get_app("app", force_create=True)
CORS(app)
DB_FILE = "lite.db"
generate_schema = False if os.path.exists(DB_FILE) else True
register_tortoise(app, db_url=f"sqlite://{DB_FILE}",
                  modules={"models": ["models"]},
                  generate_schemas=generate_schema)
app.run(debug=True, port=8000, host='0.0.0.0')
