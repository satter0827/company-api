from flask import Flask, make_response, jsonify
from .views import company_router

def create_app():

  app = Flask(__name__)
  app.register_blueprint(company_router, url_prefix='/api')

  return app

app = create_app()