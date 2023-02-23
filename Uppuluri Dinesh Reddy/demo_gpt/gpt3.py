import openai
import pandas as pd
from flask import Flask, render_template, request

openai.api_key = ""
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def gpt3_response():
    if request.method == 'POST':
        df = pd.read_csv(r'C:\Users\UppuluriDineshReddy\Downloads\data_gpt3.csv')
        df.dropna()
        df1 = df.iloc[650:]

        pre_text = df1.to_json(orient="records")

        query = request.form.get('question')
        response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=pre_text + "\n" + str(query),
                    temperature=0.7,
                    max_tokens=2048,
                    top_p=0,
                    frequency_penalty=0,
                    presence_penalty=0,
                    best_of=1,
                    stop=None)

        res = response.choices[0].text
        return render_template('demo.html', inputs=res, question=query)

    return render_template('demo.html')


if __name__ == "__main__":
    app.run(debug=True)
