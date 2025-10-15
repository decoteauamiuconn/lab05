"""Basic requirements
1. All subscribers are stored in the HTTP server.
2. There is one endpoint for adding a subscriber – each subscriber is a name and a URL
3. There is one endpoint for deleting subscribers – supplying only the subscriber's name
4. There is one endpoint for returning a list of subscribers and their URLs
5. There is one endpoint for updating the published subject and notifying all subscribers
a. The notifications can be print statements on the backend
b. The backend should be run in one terminal and another terminal should be used
for testing with curl"""

#compare with last lab; also used pub/sub

from flask import Flask, request, jsonify
import json
#import httpx <- used in previous labs, not this one


# Define the Flask app
app = Flask(__name__)

subscribers = {}

def home():
  return "Hello from Flask!"

@app.route('/', methods=['GET'])
def root():
  return jsonify("hello at the root")

#requirement 4
@app.route('/list-subscribers', methods=['GET'])
def listSubscribers():
  return jsonify(subscribers)

# Windows> curl.exe -X POST -H "Content-Type: application/json" -d "{\"name\":\"Alice\",\"URI\":\"http://good.site.com\"}" http://localhost:5000/add-subscriber

#requirement 1
@app.route('/add-subscriber', methods=['POST'])
def addSubscriber():
  data = request.json
  name = data.get('name')
  URI = data.get('URI')
  subscribers[name] = URI
  print(f"You entered: Name={name}, Address={URI}")
  return jsonify({'message': f'You sent name: {name} and address: {URI}'})

#not example code; mine

#requirement 3
@app.route('/remove-subscriber', methods=['POST'])
def removeSubscriber():
  data = request.json
  name = data.get('name')
  subscribers.pop(name)  #insisted on .pop, not del subscribers
  print(f"Removed the subscriber {name}.")
  return 'You removed subscriber: ' + name

#requirement 5
@app.route('/update-for-subscribers', methods=['POST'])
def updateSubscribers():
    data = request.json
    message = data.get('message')
    print(f"Notifying all subscribers with message: {message}") #backend print statement
    for key in subscribers.keys():
        print(f"Notified {key} at {subscribers[key]} with message: {message}")
    return jsonify({'message': f'Notified all subscribers with message: {message}'})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)