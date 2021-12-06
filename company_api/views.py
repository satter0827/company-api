from flask import Blueprint, request, make_response, jsonify, render_template
from company_api.models import Company, CompanySchema
import json

company_router = Blueprint('company_router', __name__)

@company_router.route('/', methods=['GET'])
def get_index():
  return render_template('index.html')

#Company参照用URL
@company_router.route('/companies', methods=['GET'])
def getCompanyList():

  companies = Company.getCompanyList()
  company_schema = CompanySchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'companies': company_schema.dump(companies).data
  }))

#Company登録用URL
@company_router.route('/companies', methods=['POST'])
def registCompany():

  print(request.json)

  jsonData = json.dumps(request.json)
  companyData = json.loads(jsonData)

  company = Company.registCompany(companyData)
  company_schema = CompanySchema(many=True)

  return make_response(jsonify({
    'code': 200,
    'company': company
  }))