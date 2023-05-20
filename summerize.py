# This Python file uses the following encoding: utf-8
import cohere
from googletrans import Translator
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi


co = cohere.Client('PlUWaTH2F6AkPZ3YpD0jLE7CkWsRcRClMdnvHcHh') # This is your trial API key


transcript = YouTubeTranscriptApi.get_transcript('MT8mUsrShEk')
txtlist=[]
for i in transcript:
    outtxt = (i['text'])
    txtlist.append(outtxt)

txtlist = ' '.join(txtlist)
text = txtlist[:10000]



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



response = co.summarize(
  text=text,
  length='long',
  format='paragraph',
  model='summarize-xlarge',
  additional_command='write it as a preview, very general, write it as a description',
  temperature=0.1,
  extractiveness='auto',
  )

summery = response.summary

translator = Translator()
translated = translator.translate(summery,src='en',dest='ar')
print(translated.text)

