#python file
import os
import openai
import gradio as gr

openai.api_key = "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"

start_sequence="\nAI:"
restart_sequence="\nHuman:"

prompt="ASK HERE✍️✍️✍️✍️✍️)"

def openai_create(prompt):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=["Human:", "AI:"]
)

    return response.choices[0].text # type: ignore

def chatgpt_clone(input,history):
    history=history or []
    s=list(sum(history,()))
    s.append(input)
    inp=''.join(s)
    output=openai_create(inp)
    history.append((input,output))
    return history,history   

block=gr.Blocks()

with block:
    gr.Markdown("""<h1><center><marquee>CHAT_GPT CLONE</center></h1>
    """)
    chatbot=gr.Chatbot()
    message=gr.Textbox(placeholder=prompt)
    state=gr.State()   
    submit=gr.Button("SEND")
    submit.click(chatgpt_clone, inputs=[message,state], outputs=[chatbot, state])
 
from requests.exceptions import ConnectionError
try:
    r=block.launch(share=True, auth=("shivam", "ppl@123"),debug=True,show_api=False)
except ConnectionError as e:
    print 
    r="No response"