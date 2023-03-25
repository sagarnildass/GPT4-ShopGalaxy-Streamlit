import streamlit as st
import requests
import json
import requests
from io import BytesIO




st.set_page_config(
    page_title="GPT4 Chat - Demo",
    page_icon=":robot:",
    layout="wide"
)




API_URL = "https://beam.slai.io/a8vki"
headers = {
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate",
  "Authorization": "Basic NWRjMWI2NTQ0YjFjZjEzZmNiMTM3YjM1OTc3YjRmMjE6MzU2NzY5ZGJhM2FiZDhjYjY0MGNhMTJmYzBmY2JjYjE=",
  "Connection": "keep-alive",
  "Content-Type": "application/json"
}


st.header("ShopGPT-4")

gender = st.radio(
    "Select your gender 👇",
    ["menswear", "womenswear"],
    key="gender"
    )



def query(payload):
    response = requests.request("POST", API_URL, headers=headers, data=json.dumps(payload))
    return response.json()

def clear_text():
    st.session_state["input"] = ""

def get_text():
    input_text = st.text_input("You: ","", key="input")
    return input_text 

if __name__ == "__main__":

    


    user_input = get_text()
    if st.button("Send"):

        if "reset" in user_input.lower():
            payload = {
                "query":{
                    "text": user_input,
                },
                "identifier":"sagarnil",
                "gender":gender,
            }
            output = query(payload)
            st.header("Chat Reseted!")

    
        elif gender and not "reset" in user_input.lower():
            payload = {
            "query":{
                "text": user_input,
            },
            "identifier":"sagarnil",
            "gender":gender,
        }
            output = query(payload)
 

            col1, col2, col3, col4, col5, col6 = st.columns(6)
            headline = []
            copy = []
            search = []

            for i in output['prompt']:
                headline.append(i['headline'])
                copy.append(i['copy'])
                search.append(i['search_terms'])

        

            with col1:
                st.header(headline[0])
                st.subheader(copy[0])
                st.caption(search[0])


            with col2:
                st.header(headline[1])
                st.subheader(copy[1])
                st.caption(search[1])

            with col3:
                st.header(headline[2])
                st.subheader(copy[2])
                st.caption(search[2])

            with col4:
                st.header(headline[3])
                st.subheader(copy[3])
                st.caption(search[3])

            with col5:
                st.header(headline[4])
                st.subheader(copy[4])
                st.caption(search[4])

            with col6:
                st.header(headline[5])
                st.subheader(copy[5])
                st.caption(search[5])

 

        
        
