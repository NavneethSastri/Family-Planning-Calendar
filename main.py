from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


events = [
		{"id": 1, "title": "Family Picnic", "date": "2023-11-01"},
		{"id": 2, "title": "Birthday Party", "date": "2023-11-15"}
]

@app.route('/')
def index():
		return render_template('index.html', events=events)

@app.route('/events', methods=['POST'])
def add_event():
		data = request.get_json()
		new_event = {
				"id": len(events) + 1,
				"title": data['title'],
				"date": data['date']
		}
		events.append(new_event)
		return jsonify({"message": "Event added successfully"}), 201


if __name__ == '__main__':
		app.run(host='0.0.0.0', port=81)
