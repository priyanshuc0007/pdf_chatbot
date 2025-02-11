import gradio as gr
from chatbot import get_response

def chat_interface(user_input, history):
    response = get_response(user_input)
    history.append((user_input, response))
    return history, history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    state = gr.State([])
    with gr.Row():
        user_input = gr.Textbox(show_label=False, placeholder="Enter your question...")
        submit_btn = gr.Button("Send")
    submit_btn.click(chat_interface, inputs=[user_input, state], outputs=[chatbot, state])

demo.launch(share=True)
