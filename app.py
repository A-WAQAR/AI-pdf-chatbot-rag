import streamlit as st
import requests

st.set_page_config(page_title="PDF AI Chatbot",
                   page_icon="📄")
st.title("📄PDF AI Chatbot")
st.write("ask question about your uploaded document.")
question = st.text_input("enter your question: ")

if st.button("Ask AI"):
    if not question.strip():
        st.warning("Please enter a question.")
    else:
        try:
             
            with st.spinner("searching document...."):
            
                response = requests.post("http://api:8000/ask", 
                                        json={"question": question},
                                        timeout=30)

            if response.status_code == 200:
                result = response.json()
                st.success("Answer")
                st.write(result["answer"])
            else:
                st.error("something went grong")   
        except requests.exceptions.ConnectionError:
            st.error("could not connect to the fastapi server. " "please make sure the API is running")
        except requests.exceptions.Timeout:
            st.error("the request timed out. please try again")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
        except Exception as e:
            st.error( f"Something went wrong: {e}" )








