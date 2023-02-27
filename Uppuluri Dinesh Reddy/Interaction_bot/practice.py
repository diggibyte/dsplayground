import openai
import gradio as gr
import pandas as pd

openai.api_key = "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"

start_sequence = "\nAI:"
stop_sequence = "\nHuman:"

# df = pd.read_csv(r'C:\my_folder\data\data.csv')
df = pd.read_csv(r'C:\Users\UppuluriDineshReddy\Downloads\data_gpt3.csv')
df.dropna()
df1 = df.iloc[650:]
record_str = df1.to_json(orient="records")

# prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:"
prompt = ''
def openai_create(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + "\n" + str(record_str),
        temperature=0.9,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
    return response.choices[0].text

def conversational_history(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = " ".join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history

blocks = gr.Blocks()

with blocks:
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder=prompt)
    state = gr.State()
    submit = gr.Button("click")
    submit.click(conversational_history, inputs=[message, state], outputs=[chatbot, state])

blocks.launch(debug=True)
