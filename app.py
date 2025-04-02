import gradio as gr
from transformers import pipeline

# Load mô hình tóm tắt từ Hugging Face
summarizer = pipeline("summarization", model="NlpHUST/t5-small-vi-summarization")

def summarize(text):
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]['summary_text']

# Giao diện Gradio
iface = gr.Interface(fn=summarize, 
                     inputs=gr.Textbox(lines=10, placeholder="Nhập văn bản cần tóm tắt..."), 
                     outputs="text",
                     title="Vietnamese News Summarizer",
                     description="Nhập văn bản tiếng Việt và nhận lại bản tóm tắt ngắn gọn.")

iface.launch()
