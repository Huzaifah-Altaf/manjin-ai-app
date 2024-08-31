import streamlit as st
from groq import Groq
client = Groq(api_key='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')
# website name 
st.title('Manjin AI') 
st.subheader('By Huzaifah Altaf')
st.write('---')
st.text('\n'*3)
st.write('Ask me anything')

def main():
    message = st.text_input('Write the Question here')
    if st.button('Submit'):
        st.write('You asked:', message)
        chat_completions = client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages = [
                {
                   "role":"user",
                   'content':message

                }
                
            ],      


        )
        if chat_completions:
            st.write('MANJIN : '+ chat_completions.choices[0].message.content)
        else:
            st.write('No response from the bot')
if __name__ == '__main__':
    main()
