from analytics_app import create_app

application = create_app()
app = application

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
