import streamlit as st
import time
import numpy as np
import pandas as pd
import plotly.express as px


global numM

#################################### Function to simulate typing  ####################################
def stream_data(reply):
    for word in reply.split():
        yield word + " "
        time.sleep(0.2)

#################################### Handle Interactions  ####################################
def interactionHandler():
    global numM 
    #Check if user wants to cogntinue
    print(numM)
    if len(st.session_state["messages"]) == 4 :
        reply = "Have you heard of this company? Please answer with '**yes**' or '**no**'."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 1
    if prompt.lower()  == "yes" and numM == 1:
        reply = ("Oh Wow! That's great! ")
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 6
        time.sleep(2)
        continue1()
    if prompt.lower() == "no" and numM == 1:
        reply = ("Ohh, don't worry about it, I will explain everything to you!")
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 6
        continue1()
    if prompt.lower() == "ready":
        numM = 15
        continue1()
    
    #################################### Graph for Success rates  ####################################
def plot_success_rates(success_rates):
    df = pd.DataFrame(list(success_rates.items()), columns=['Strategy', 'Success Rate'])
    fig = px.bar(df, x='Strategy', y='Success Rate', labels={'Strategy': 'Strategy', 'Success Rate': 'Success Rate'}, title='Success Rates of Strategies',
                 text='Success Rate',  color='Strategy', template='plotly_white')  
    fig.update_layout(xaxis_title='Strategy',yaxis_title='Success Rate',font=dict(family='Arial, sans-serif', size=12, color='RebeccaPurple'),
        plot_bgcolor='rgba(0,0,0,0)', yaxis=dict(range=[0,1]))
    
    fig.update_traces(marker_line_width=1.5, opacity=0.6) 
    st.plotly_chart(fig)

    #################################### Intro  ####################################
def intro():
    #Intro Messages
    global numM
    numM = 1
    if len(st.session_state["messages"]) == 2:
        time.sleep(2)
        reply = "Nice to meet you " + str(prompt) + "! Let's go ahead and get started working on this case."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
    

    if len(st.session_state["messages"]) == 3 :
        reply = ("I’ll explain a bit about the company: Hunter LLC is a big player in the construction "
                 + "segment in the US. They have been in this industry for a "
                 + "long time and lately they have been looking for some new opportunities.")
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))   
    interactionHandler()

#################################### Conversation  ####################################
def continue1():
    global numM
    if numM == 6 :
        reply = "Let's move on then. After their last annual meeting, they decided they want to make some new investments. Therefore, they have discussed the annual financial targets, setting the goals fo the upcoming year"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 8

    if numM == 8 :
        reply = "To achieve these, we've been evaluating different strategies and have narrowed down to two distinct options."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 9 :
        reply = "Here are the two options we're considering:"
        time.sleep(2)
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 10:
        reply = "**Option A**: This option grows your money slowly. It’s like putting your money in a safe place where it can grow bit by bit."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 11:
        reply = "**Option B**: This option is for taking chances to possibly make more money. It's an alternate strategy, but it could lead to better results."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 12:
        reply = "Ok, so those are the options we have, I went ahead and calculated the success rates for each option. I would love to show them to you!"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM += 1

    if numM == 13:
        reply = "Please type '**ready**' when you are ready to see the success rates."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 14

    if numM == 15 :
        reply = ("Great. So, according to my calculations, the success rate"
                 + " for Option A is 81%") + " and for Option B is 63%"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        success_rates = {"Option A": 0.81, "Option B": 0.63}
        plot_success_rates(success_rates)
        numM += 1

    if numM == 16 :
        with st.spinner("Thinking..."):
            time.sleep(5)

            reply = ("Based on the calculation, we have decided to go"
                 + " for option A Let us wait for the results to be printed!")
            st.session_state["messages"].append({"role": "assistant", "content": reply})
            st.chat_message("assistant").write_stream(stream_data(reply))
            numM = 18

    if numM == 18 :
        reply = "Please wait for the results to be printed."
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        numM = 19

    if numM == 19 :
        reply = "Thank you for your time and cooperation!"
        st.session_state["messages"].append({"role": "assistant", "content": reply})
        st.chat_message("assistant").write_stream(stream_data(reply))
        

#################################### Main  ####################################
prompt = st.chat_input()

st.title("💬 Pepper")
st.caption("🚀 Your business advisor/consultant")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello, my name is Pepper, and today I am going "
                                                                     + "to guide you trough solving a business "
                                                                     + "case for Hunter LLC. **What is your name?**"}]

for msg in st.session_state["messages"]:
     st.chat_message(msg["role"]).write(msg["content"])

if prompt:
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    intro()


