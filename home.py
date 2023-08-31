from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime, date
import random
import string


app = Flask(__name__)

today = datetime.combine(date.today(), datetime.min.time())  # Convert to datetime

# Admin dashboard
@app.route('/')
def admin_dashboard():
    return render_template('admin.html', coupons=coupons.find(), today=today)  # Pass 'today' to the template

client = MongoClient('mongodb://localhost:27017/')
db = client['coupon']
coupons = db['creates']

def generate_coupon_code(length=8):
    characters = string.ascii_uppercase + string.digits
    coupon_code = ''.join(random.choice(characters) for _ in range(length))
    return coupon_code

# Format date
def format_date(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    year = date_obj.year
    month = date_obj.month
    day = date_obj.day
    return datetime(year, month, day)

def get_coupon(coupon_id):
    return coupons.find_one({'_id': coupon_id})

# Generate coupon route
@app.route('/generate_coupon', methods=['POST'])
def generate_coupon():
    if request.method == 'POST':
        coupon_code = generate_coupon_code()
        discount = int(request.form['discount'])
        start_date = format_date(request.form['start_date'])
        expire_date = format_date(request.form['expire_date'])

        # Create the coupon in your MongoDB
        coupons.insert_one({'code': coupon_code, 'discount': discount, 'start_date': start_date, 'expire_date': expire_date})

        return f'Generated Coupon Code: {coupon_code}'

# Check expiration route
@app.route('/check_expire/<coupon_id>', methods=['GET'])
def check_expire(coupon_id):
    coupon = get_coupon(coupon_id)  # Implement your get_coupon function here

    if coupon and coupon['expire_date'] > datetime.now():
        return "Valid"
    else:
        return "Expired"

# Admin dashboard
# @app.route('/')
# def admin_dashboard():
#     return render_template('admin.html', coupons=coupons.find())

# Admin create coupon
@app.route('/admin/create', methods=['POST'])
def admin_create_coupon():
    if request.method == 'POST':
        code = request.form['code']
        discount = int(request.form['discount'])
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        expire_date = datetime.strptime(request.form['expire_date'], '%Y-%m-%d')
        coupons.insert_one({'code': code, 'discount': discount, 'start_date': start_date, 'expire_date': expire_date})
    return redirect(url_for('admin_dashboard'))

if __name__ == '__main__':
    app.run(debug=True)
