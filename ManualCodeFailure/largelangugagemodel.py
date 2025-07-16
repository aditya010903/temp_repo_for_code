from transformers import pipeline
import gradio as gr

# Ensure TensorFlow is imported to avoid any runtime issues
# import tensorflow as tf

# Initialize the chatbot pipeline
chatbot = pipeline(model="facebook/blenderbot-400M-distill")
message_list = []
response_list = []

def vanilla_chatbot(message, history):
    conversation = chatbot(message)
    return conversation[0]['generated_text']

demo_chatbot = gr.ChatInterface(vanilla_chatbot, title="Vanilla Chatbot", description="Enter text to start chatting.")

demo_chatbot.launch()