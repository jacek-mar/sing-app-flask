"""
Flask Sing App - Application Entry Point
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Import and run the application
from app import create_app

app = create_app()

if __name__ == '__main__':
    port = int(os.environ.get('FLASK_RUN_PORT', 49251))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=os.environ.get('FLASK_ENV') == 'development'
    )
