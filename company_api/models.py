from company_api.database import db, ma

class Company(db.Model):
  __tablename__ = 'companies'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  description = db.Column(db.String(128), nullable=False)
  url = db.Column(db.String(128), nullable=False)

  def __repr__(self):
    return '<Company %r>' % self.name

  def getCompanyList():
    # select * from companies
    company_list  = db.session.query(Company).all()

    if company_list  == None:
      return []
    else:
      return company_list 

  def registCompany(company):
    record = Company(
      name = company['name'],
      description = company['description'],
      url = company['url'],
    )
   
    # insert into company(name, address, tel, mail) values(...)
    db.session.add(record)
    db.session.commit()

    return company

class CompanySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
      model = Company
      fields = ('id', 'name', 'description', 'url')
