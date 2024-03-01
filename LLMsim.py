import streamlit as st
import time
import numpy as np
import pandas as pd

st.title("💬 Pepper")
st.caption("🚀 Your business advisor/consultant")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, I'm Pepper and today I am going to guide you through solving a business case for Hunter LLC. But before we start, please let me know your name!"}]
    #st.session_state["messages"].append({"role": "assistant", "content": "But before we start, please let me know your name!"})

# Func for displaying messages as typing
def stream_data(reply):
    for word in reply.split():
        yield word + " "
        time.sleep(0.1)

# Displaying past messages
for msg in st.session_state["messages"]:
     st.chat_message(msg["role"]).write(msg["content"])



# Handling new input
prompt = st.chat_input()
if prompt :
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

if prompt and len(st.session_state["messages"]) == 2 :
    reply = "Nice to meet you! Let's go ahead and get started working on this case."
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))

if prompt and len(st.session_state["messages"]) == 2 :
    reply = "Ok. let’s get to it right now! I’ll explain a bit about the company. Hunter LLC specializes in high-value financial solutions particularly for affluent families aiming to optimize their investments."
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))

if prompt and len(st.session_state["messages"]) == 3 :
    reply = "Recently we discussed the annual financial targets with a major client family, setting ambitious but attainable goals."
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))

if prompt and len(st.session_state["messages"]) == 4 :
    reply = "To achieve these, we've been evaluating various strategies and have narrowed down to two distinct paths. However, there seems to be a bit of a dilemma in finalizing our approach."
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))

if prompt and len(st.session_state["messages"]) == 5 :
    reply = "Here are the two strategies we're considering: Option 1: Low-Risk Funds - These are the usual secure investment avenues like government bonds or stable market funds. Traditionally they're low yield but very safe."
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))

if prompt and len(st.session_state["messages"]) == 6 :
    reply = "Option 2: High-Growth Sectors - Investments focusing on sectors like technology or healthcare known for volatility but potentially higher returns."
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))

if prompt and len(st.session_state["messages"]) == 7 :
    reply = "Ok, so those are the options we came up with, according to my findings the best option for this family is certainly Option 1"
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))

if prompt and len(st.session_state["messages"]) == 7 :
    reply = "Please reply yes if you agree, ........ Decide what to put here"
    st.session_state["messages"].append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write_stream(stream_data(reply))





        
