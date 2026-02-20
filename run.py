"""
Flask Sing App - Application Entry Point
"""
import os
from dotenv import load_dotenv

# Load environment variables — single authoritative load point
load_dotenv()

from app import create_app

config_name = os.environ.get('FLASK_CONFIG', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_RUN_PORT', 49251))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=app.debug
    )
