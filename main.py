from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

from flash_flask import App
from flash_flask.db import MySQL

from flask_cors import CORS

import os
import dotenv

dotenv.load_dotenv()

app = App(__name__)

CORS(app.flask)

MySQL.init(os.getenv("MYSQL_HOST"), os.getenv("MYSQL_PORT"), os.getenv("MYSQL_USER"), os.getenv("MYSQL_PASSWORD"), os.getenv("MYSQL_DATABASE"))

def delete_expired_messages():
    MySQL.delete("messages", "created_at < %s", (datetime.now() - timedelta(days=7),))

if __name__ == "__main__":

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=delete_expired_messages, trigger="interval", hours=24)
    scheduler.start()

    app.run(debug=True)