# # Import required modules
# from flask import Flask, render_template, request, redirect, url_for
# from pymongo import MongoClient
# import random
# import string

# # Create Flask app
# app = Flask(__name__)

# # Connect to MongoDB
# client = MongoClient('mongodb://localhost:27017/')
# db = client['coupon_db']
# coupons = db['coupons']

# # Coupon code generation function
# def generate_coupon_code(length=8):
#     characters = string.ascii_uppercase + string.digits
#     coupon_code = ''.join(random.choice(characters) for _ in range(length))
#     return coupon_code

# # Home page
# @app.route('/')
# def index():
#     return render_template('index.html', coupons=coupons.find())

# # Create coupon page
# @app.route('/create', methods=['GET', 'POST'])
# def create_coupon():
#     if request.method == 'POST':
#         discount = request.form['discount']
#         code = generate_coupon_code()  # Generate random coupon code
#         coupons.insert_one({'code': code, 'discount': discount})
#         return redirect(url_for('index'))
#     return render_template('create_coupon.html')

# # Scratch coupon page (new)
# @app.route('/scratch', methods=['GET', 'POST'])
# def scratch_coupon():
#     if request.method == 'POST':
#         code = request.form['code']
#         coupon = coupons.find_one({'code': code})
#         if coupon:
#             return f"Scratch the coupon to reveal {coupon['discount']}% discount!"
#         else:
#             return "Invalid Coupon Code"
#     return render_template('scratch_coupon.html')  # Create this HTML file

# # Run the app
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['coupon']
coupons = db['creates']

# ... Other functions and routes ...

# Admin dashboard
@app.route('/')
def admin_dashboard():
    return render_template('admin.html', coupons=coupons.find())

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

