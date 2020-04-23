import flask

#df = pd.read_csv("https://github.com/bgweber/Twitch/raw/master/Recommendations/games-expand.csv")
#model = LogisticRegression()
#model.fit(df.drop(['label'], axis=1), df['label'])

app = flask.Flask(__name__)

@app.route("/", methods=["GET","POST"])
def predict():
    data = {"success": False}

    return flask.jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
