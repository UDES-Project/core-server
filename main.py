from flash_flask import App
from flash_flask.db import MySQL

import os
import dotenv

dotenv.load_dotenv()

app = App(__name__)

MySQL.init(os.getenv("MYSQL_HOST"), os.getenv("MYSQL_PORT"), os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), "umes")

if __name__ == "__main__":
    app.run(debug=True)