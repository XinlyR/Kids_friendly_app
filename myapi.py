from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///locations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    vicinity = db.Column(db.String(100))
    zip_code = db.Column(db.String(10))
    type = db.Column(db.String(50))

# Uncomment this line once to initialize the database
# db.create_all()

@app.route('/')
def index():
    return "Welcome to the Kids-Friendly Locations API!"

@app.route('/api/locations', methods=['GET'])
def get_locations():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    locations = Location.query.paginate(page=page, per_page=per_page, error_out=False)
    
    data = [{
        'id': location.id,
        'name': location.name,
        'vicinity': location.vicinity,
        'zip_code': location.zip_code,
        'type': location.type
    } for location in locations.items]

    return jsonify({
        'page': page,
        'per_page': per_page,
        'total': locations.total,
        'locations': data
    })

@app.route('/api/locations/<int:id>', methods=['GET'])
def get_location(id):
    location = Location.query.get_or_404(id)
    data = {
        'id': location.id,
        'name': location.name,
        'vicinity': location.vicinity,
        'zip_code': location.zip_code,
        'type': location.type
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)