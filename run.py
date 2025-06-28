from mflix.factory import create_app
from configparser import ConfigParser
from mflix.db import init_app as init_db

# Load MongoDB URI from sample.ini
config = ConfigParser()
config.read("sample.ini")

mongo_uri = config["APP"]["DB_URI"]  # Make sure your [APP] section exists

if __name__ == "__main__":
    # Create the app with injected config
    app = create_app({
        "DEBUG": True,
        "MONGO_URI": mongo_uri
    })

    # Initialize DB connection
    init_db(app)

    # Run the app
    app.run()