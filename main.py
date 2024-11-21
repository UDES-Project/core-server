from flash_flask import App
from flash_flask.db import MySQL

from flask_cors import CORS

import os
import dotenv
import logging

dotenv.load_dotenv()

app = App(__name__)

handler = logging.FileHandler("logs/flask.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
)
handler.setFormatter(formatter)

app.flask.logger.addHandler(handler)

CORS(app.flask)

MySQL.init(os.getenv("MYSQL_HOST"), os.getenv("MYSQL_PORT"), os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_DATABASE"))

if __name__ == "__main__":
    app.run(debug=True)