from youtube_transcript_api import YouTubeTranscriptApi

transcript = YouTubeTranscriptApi.get_transcript('pJ0auP7dbcY&t')
txtlist=[]
for i in transcript:
    outtxt = (i['text'])
    txtlist.append(outtxt)
print(txtlist[:500])

