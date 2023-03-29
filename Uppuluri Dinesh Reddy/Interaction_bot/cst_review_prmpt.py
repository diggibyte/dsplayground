import openai
import os
import pandas as pd
from flask import Flask, render_template, request

openai.api_key = "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"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def gpt3_response():
    if request.method == 'POST':
        df = pd.read_csv(r'C:\Users\UppuluriDineshReddy\Downloads\sales_demo_data(modified).csv')
        df.dropna()
        df1 = df.iloc[:15]

        pre_text = df1.to_json(orient="records")
        query = request.form.get('question')
        # prompt = f"""Answer the question based on the content without grammatical errors and find the pattern between the query and data to respond the questions like for example why or which\n
        # If the question cannot be answered or not related\n then answer "I don't know Ask related to domain."
        # content: {query}
        # """

        prompt = f"""Understand the question based on the content properly and respond with a sentence and find the exact pattern between the query and data to respond the questions like for example why or which\n
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
                        temperature=0.5,
                        max_tokens=100,
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
