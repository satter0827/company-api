from flask import Blueprint, request, make_response, jsonify, render_template
import os

company_router = Blueprint('company_router', __name__)

@company_router.route('/', methods=['GET'])
def get_index():
  os.getcwd()
  return render_template('index.html')

@company_router.route('/company', methods=['GET'])
def get_user_list():
  return make_response(jsonify({
    'companies': [
       {
         'id': 1,
         'name': 'DL生命'
       }
     ]
  }))