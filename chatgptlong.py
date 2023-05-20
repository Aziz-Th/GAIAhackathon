# py -m pip install -r requirements.txt

# This Python file uses the following encoding: utf-8
from googletrans import Translator
import streamlit as st
import streamlit.components.v1 as components

from youtube_transcript_api import YouTubeTranscriptApi

import openai
import os

import pandas as pd

import time

openai.api_key = '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'

sumsum=''
def summerize(paragraph,creativity,language):
    if '=' in paragraph:
        paragraph=paragraph.split('=')
        paragraph = (paragraph[1])
    else:
        paragraph=paragraph.split('/')
        paragraph=paragraph[-1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(paragraph,languages=['en', 'ar'])

        txtlist = []
        for i in transcript:
            outtxt = (i['text'])
            txtlist.append(outtxt)
        txtlist = ' '.join(txtlist)
        transcript_length = len(txtlist)
        # for t in range(0,int(transcript_length/10000)):
        #     text = txtlist[t:t+10000]
        text=txtlist[:10000]



        # translator = Translator()
        # translated = translator.translate(summery, src='en', dest='ar')

        def get_completion(prompt, model="gpt-3.5-turbo"):

            messages = [{"role": "user", "content": prompt}]

            response = openai.ChatCompletion.create(

                model='gpt-3.5-turbo',

                messages=messages,

                temperature=0,

            )

            return response.choices[0].message["content"]

        # prompt = f"You are tasked with summerizing what the following podcast content is about briefly, Please summarize the following text in arabic,:{text}"

        if language == 'Arabic':
            lang='arabic'
        else:
            lang='english'

        prompt = f"you are tasked with summarizing a segment in the following podcast, Please summarize the following text in {lang} briefly,:{text}"

        response = get_completion(prompt)
        return response




    except:
        return "This video can't be summarized because it has no captions"





langs=['Arabic','English']
st.title("Podcast Summarizer")
form = st.form(key="user_settings")
with form:
    para_input = st.text_input("URL", key = "link_input")
    Creativity = st.slider('Creativity',min_value=1,max_value=10,value=3,help='Indicates The Randomness of The Summarization',)
    lang = st.selectbox('Language',options=langs)
    generate_button = form.form_submit_button("Summarize")
    if generate_button:
        sumsum = summerize(para_input,Creativity,lang)
        st.write(sumsum)

    st.components.v1.html((f'<a href="https://twitter.com/intent/tweet?text={sumsum}" class="twitter-share-button" data-show-count="false">Tweet</a><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>'), scrolling=False)

