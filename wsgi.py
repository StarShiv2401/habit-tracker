from waitress import serve
from app import create_app

# Create the Flask application using your factory function
app = create_app()

if __name__ == "__main__":
    # Print startup message
    print("Starting Habit Tracker on http://0.0.0.0:8080")

    # Serve the application with Waitress
    # You can adjust host/port as needed
    serve(app, host="0.0.0.0", port=8080)