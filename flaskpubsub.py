# example code provided by professor

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


# Define the Flask app
app = Flask(__name__)

subscribers = {}

def home():
  return "Hello from Flask!"

@app.route('/', methods=['GET'])
def root():
  print(f"Hello at the root")
  return jsonify({'main endpoint':'Ack'})

@app.route('/list-subscribers', methods=['GET'])
def listSubscribers():
  return jsonify(subscribers)

# Windows> curl.exe -X POST -H "Content-Type: application/json" -d "{\"name\":\"Alice\",\"URI\":\"http://good.site.com\"}" http://localhost:5000/add-subscriber

@app.route('/add-subscriber', methods=['POST'])
def addSubscriber():
  data = request.json
  name = data.get('name')
  URI = data.get('URI')
  subscribers[name] = URI
  print(f"You entered: Name={name}, Address={URI}")
  return jsonify({'message': f'You sent name: {name} and address: {URI}'})

#not example code; mine
  @app.route('/remove-subscriber', methods=['POST'])
def removeSubscriber():
  data = request.json
  name = data.get('name')
  subscribers.remove("name") 
  print(f"Removed the subscriber {name}.")
  return jsonify({'message': f'You removed subscriber: {name}'})

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)