from youtube_transcript_api import YouTubeTranscriptApi

transcript = YouTubeTranscriptApi.get_transcript('pJ0auP7dbcY&t')
txtlist=[]
for i in transcript:
    outtxt = (i['text'])
    txtlist.append(outtxt)

txtlist = ' '.join(txtlist)
# print(txtlist[:10000])
print(transcript[0]['start'])

