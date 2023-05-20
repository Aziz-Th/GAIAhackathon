# This Python file uses the following encoding: utf-8
import cohere
from googletrans import Translator
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import openai
import os

import pandas as pd

import time

# openai.api_key = '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'

co = cohere.Client('PlUWaTH2F6AkPZ3YpD0jLE7CkWsRcRClMdnvHcHh') # This is your trial API key


transcript = YouTubeTranscriptApi.get_transcript('pJ0auP7dbcY&t')
txtlist=[]
for i in transcript:
    outtxt = (i['text'])
    txtlist.append(outtxt)

txtlist = ' '.join(txtlist)
text = txtlist[:3000]

def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "user", "content": prompt}]

    response = openai.ChatCompletion.create(

    model='gpt-3.5-turbo',

    messages=messages,

    temperature=0,

    )

    return response.choices[0].message["content"]

# prompt = f"You are tasked with summerizing what the following podcast content is about briefly, Please summarize the following text in arabic,:{text}"

prompt = f"you are tasked with summarizing a segment in the following podcast, Please summarize the following text in arabic briefly,:{text}"


response = get_completion(prompt)

print(response)
# def summerize(paragraph):
#   brief = co.summarize(
#     text=paragraph,
#     length='short',
#     format='paragraph',
#     extractiveness='low',
#     model='summarize-xlarge',
#     additional_command='',
#     temperature=0.3,)
#   translator = Translator()
#   translated = translator.translate(brief, src='en', dest='ar')
#   return translated.text

# st.title("🚀 Startup Idea Generator")
# form = st.form(key="user_settings")
# with form:
#     para_input = st.text_input("text", key = "text_input")
#     generate_button = form.form_submit_button("summerize")
#     if generate_button:
#         sumsum = summerize(para_input)
#         st.write(sumsum)


# summery = response.summary
#
# translator = Translator()
# translated = translator.translate(summery,src='en',dest='ar')
# print(translated.text)

