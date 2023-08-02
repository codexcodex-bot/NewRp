from website_project.app import create_app
from website_project.config import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == "__main__":
    app.run()