import pickle
import flask
import os
import pandas as pd 

app = flask.Flask(__name__)
port = int(os.getenv("PORT", 9099))

model = pickle.load(open("model.pkl","rb"))

@app.route('/predict', methods=['POST', 'GET'])
def predict():

	features = flask.request.get_json()

	start = features["start"]
	end = features["end"]
	#dti = pd.date_range('2019-01-03 23:35:00', periods=5, freq='5S')
	dti = pd.date_range('2019-01-03 23:35:00', periods=5, freq='5min')
	print (dti)


	features = flask.request.get_json(force=True)
	#horizon = int(request.json['horizon'])

	#print (features)
	#prediction = model.predict([features])[0,0]
	prediction = model.predict(start,end,typ='levels')
	print('Forecast/preditions for 5 hours ahead ', prediction)

	response = {'prediction': prediction}
	print (response)

	#return flask.jsonify({response})

	return flask.jsonify({"result" : "sucess", "start": start, "end": end})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)
