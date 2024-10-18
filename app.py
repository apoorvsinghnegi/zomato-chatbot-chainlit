import chainlit as cl
from src.llm import ask_order, messages

@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    messages.append({"role": "user", "content": message.content}) #mesaage.content means the content it will put on the chainlit
    response = ask_order(messages) #It will give us some response.
    messages.append({"role": "assistant", "content": response})# append the response to the message

    # Send a response back to the user
    await cl.Message(
        content=response,
    ).send()