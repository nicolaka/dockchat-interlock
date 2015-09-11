from flask import Flask, render_template, request, url_for
from pymongo import MongoClient
import socket

#Mongo Settings
client = MongoClient('db', 27017) # db is the hostname for the mongodb daemon. Need to link the db container to this container and create a local alias in etc/hosts.
db = client.test_database
collection = db.test_collection
posts = db.posts

# Initialize the Flask application
app = Flask(__name__)
# Define a route for the default URL, which loads the form
@app.route('/')
def form():
	if posts.count()!=0:
		N=posts.count()
		return render_template('form_submit.html', messages=posts.find().sort('_id')[N-1]['message'],hostname=socket.gethostname())
	else:
		return render_template('form_submit.html', messages="There are no messages :)",hostname=socket.gethostname())

@app.route('/chat/', methods=['POST'])
def chat():
    message=request.form['message']
    posts.insert_one(dict(message=message))
    return render_template('form_action.html', message=message,hostname=socket.gethostname())

if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5000"),
        debug=True,
  )
