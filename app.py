from flask import Flask,render_template, request,redirect,url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')

db = client['FlaskDatabase']
collection = db['test']
collection1= db['users']

@app.route('/home') ## It is the technique used to map the specific url with the associated function to perform some task.
def home():
    return 'This is my home,page...'


@app.route('/hello/<name>')
def Profile(name):
    return f"Your Profile name is , {name}"

@app.route('/web')
def WebTemplate():
    return render_template('home.html')


@app.route('/page')
def homepage():
    list1 = ['a','e','i','o','u']
    return render_template('webpage.html',title = "Hello, Welcome to my Web page",list2=list1)

@app.route('/user')
def UserDetails():
    title = 'User Profiles'
    users = {
        "Parul" : {"age":18,"city":"nagpur"},
        "Sanyukta": {"age":22,"city":"pune"},
        "Shivani": {"age":21,"city":"mumbai"}
    }
    return render_template('profile.html',title=title,users=users)

@app.route('/add',methods=['POST'])
def add_data():
    data = request.json
    collection.insert_one(data)

    return 'Data added to mongodb'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_data',methods=['POST'])
def create_data():
    # Retrieve data from the form
    username = request.form['username']
    age = int(request.form['age'])
    city = request.form['city']

    # Create a dictionary to represent the user.
    user = {
        'username':username,
        'age':age,
        'city':city
    }
    # Insert the user into mongodb collection
    collection1.insert_one(user)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)




