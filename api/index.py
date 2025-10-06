from agents.app import app

# This is needed for Vercel to properly handle the FastAPI app
def handler(request, response):
    return app(request, response)