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

@app.route('/', methods=['GET'])
def root():
  messages=[]
  users=[]
  N=posts.count()
  if posts.count()!=0:
    for index,message in enumerate(posts.find().sort('_id')):
      messages.append(message['message'])
      users.append(message['user'])
    return render_template('form_action.html', users=users,messages=messages,hostname=socket.gethostname())
  else:
    return render_template('form_action.html', users=[],messages=[],hostname=socket.gethostname())

@app.route('/chat/', methods=['POST'])
def chat():
  user = request.form['user']
  message= request.form['message']
  posts.insert_one(dict(user=user,message=message))
  messages=[]
  users=[]
  N=posts.count()
  for index,message in enumerate(posts.find().sort('_id')):
      messages.append(message['message'])
      users.append(message['user'])
  return render_template('form_action.html', users=users, messages=messages,hostname=socket.gethostname())


if __name__ == '__main__':
  app.run( 
        host="0.0.0.0",
        port=int("5000"),
        debug=True,
  )
