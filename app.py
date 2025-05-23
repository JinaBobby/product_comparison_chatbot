import gradio 
from groq import Groq
client = Groq(
    api_key="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",
)
def initialize_messages():
    return [{"role": "system",
             "content": "You are a smart shopping assistant with deep knowledge of e-commerce platforms like Amazon, Flipkart, and others. Your role is to help users compare products, analyze features, check prices, and make informed buying decisions by offering clear, unbiased, and helpful insights."}]
messages_prmt = initialize_messages()
print(type(messages_prmt))
def customLLMBot(user_input, history):
    global messages_prmt

    messages_prmt.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        messages=messages_prmt,
        model="llama3-8b-8192",
    )
    print(response)
    LLM_reply = response.choices[0].message.content
    messages_prmt.append({"role": "assistant", "content": LLM_reply})

    return LLM_reply
  iface = gradio.ChatInterface(
    customLLMBot,
    chatbot=gradio.Chatbot(height=300),
    textbox=gradio.Textbox(placeholder="Ask me to compare products or find the best one online"),
    title="Product Comparison ChatBot",
    description="Ask me to compare products across Amazon, Flipkart, and more. I can help with features, price, and best buying options.",
    theme="soft",
    examples=["Compare iPhone 14 and Samsung S23", "Best budget laptop under ₹50,000", "Which smartwatch is better on Flipkart?"],
    submit_btn=True
)
iface.launch(share=True)
