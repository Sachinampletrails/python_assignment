from flask import Flask,jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = Flask(__name__)

# Replace with your actual MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://tekomav152:mn3eZyXMS709Md1r@pyhtondb585.4r53he.mongodb.net/?retryWrites=true&w=majority&appName=pyhtondb585"
client = MongoClient(MONGO_URI)

db = client.get_database('pythondb585')  # Assumes database name is in the URI

collection = db["newcol"]  # Replace with your collection name

@app.route('/fetch-data')
def fetch_data():
    try:
        # Find all documents in the collection
        documents = list(collection.find())

        # Convert ObjectId to string for JSON serialization
        for doc in documents:
            doc['_id'] = str(doc['_id'])

        return jsonify(documents)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')

        if not name or not email:
            error = "Name and Email are required."
            return render_template('index.html', error=error)

        try:
            collection.insert_one({'name': name, 'email': email})
            return redirect(url_for('success'))
        except PyMongoError as e:
            error = f"Database error: {str(e)}"

    return render_template('index.html', error=error)


@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
