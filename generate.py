# py -m pip install -r requirements.txt

# This Python file uses the following encoding: utf-8
import cohere
from googletrans import Translator
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi

CO_API_KEY='PlUWaTH2F6AkPZ3YpD0jLE7CkWsRcRClMdnvHcHh'
co = cohere.Client(CO_API_KEY) # This is your trial API key





def summerize(paragraph,creativity):
    if '=' in paragraph:
        paragraph=paragraph.split('=')
        paragraph = (paragraph[1])
    else:
        paragraph=paragraph.split('/')
        paragraph=paragraph[-1]

    transcript = YouTubeTranscriptApi.get_transcript(paragraph)

    txtlist = []
    for i in transcript:
        outtxt = (i['text'])
        txtlist.append(outtxt)
    txtlist = ' '.join(txtlist)
    transcript_length = len(txtlist)
    # for t in range(0,int(transcript_length/10000)):
    #     text = txtlist[t:t+10000]
    text=txtlist[:10000]
    response = co.summarize(
        text=text,
        length='long',
        format='paragraph',
        model='summarize-xlarge',
        additional_command='write it as a preview, very general, write it as a description',
        # additional_command='Write an introductory paragraph for a blog post about language models.',

        temperature=creativity/10,
        extractiveness='auto',
    )

    summery = response.summary

    translator = Translator()
    translated = translator.translate(summery, src='en', dest='ar')

    return (translated.text)


st.title("Podcast Summerizer")
form = st.form(key="user_settings")
with form:
    para_input = st.text_input("URL", key = "link_input")
    Creativity = st.slider('Creativity',min_value=1,max_value=10,value=3,help='the randomness of the summerization',)
    generate_button = form.form_submit_button("Summerize")
    if generate_button:
        sumsum = summerize(para_input,Creativity)
        st.write(sumsum)
