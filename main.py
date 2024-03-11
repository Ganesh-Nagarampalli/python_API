from flask import Flask, request, jsonify

#create a Flask application instance
app = Flask(__name__)

#when a user visits the root URL
#of this application, the function home() is called
@app.route("/")
def home():
    return "Home"

#define a route for retrieving user data
@app.route("/get-user/<user_id>")
def get_user(user_id):
    #user data for demonstration purposes
    user_data = {
        "user_id" : user_id,
        "name" : "ganesh",
        "email" : "ganeshnagarampalli@gmail.com"
    }
    #check if extra parameter is provided in the request
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    # Return user data as JSON response
    #josnify() is used to convert python dict into json format
    return jsonify(user_data), 200

#
@app.route("/create-user", methods=["POST"])
def create_user():
    #This line extracts the JSON data 
    #sent in the POST request. 
    #Flask's request object provides access to incoming request data, 
    #and get_json() is a method that parses JSON data from the request body.
    #It returns a Python dictionary representing the JSON data.
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)