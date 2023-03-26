import openai
import os
import pandas as pd
from flask import Flask, render_template, request

openai.api_key = "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"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gpt3_response():
    if request.method == 'POST':
        df = pd.read_csv(r'C:\my_folder\data\data.csv')
        df.dropna()
        df1 = df.iloc[:10]

        pre_text = df1.to_json(orient="records")
        query = request.form.get('question')
        prompt = f"""Answer the question based on the fine-tuned model.\n
        If the question cannot be answered or not related\n then answer "I don't know Ask related to domain."
        content: {query}
        """

        # query = request.form.get('question')

        if 'clear' in request.form:
            ques = ''
            inputs = ''
        else:
            response = openai.Completion.create(
                        model="text-davinci-003",
                        prompt=prompt + query + pre_text,
                        temperature=0.7,
                        max_tokens=50,
                        top_p=0,
                        frequency_penalty=0,
                        presence_penalty=0,
                        best_of=1,
                        stop=[" End"]
            )

            res = response.choices[0].text
            return render_template('visual_page.html', inputs=res, ques=query)

    return render_template('visual_page.html')


if __name__ == "__main__":
    app.run(debug=True)
