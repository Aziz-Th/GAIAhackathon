import cohere
import streamlit as st


co = cohere.Client(api_key='qjgGpoSZW5QUsl3FKx1A2sCeoVcDXQNqPidf4na0')


response = co.generate(
  prompt= st.text_input,
)
print(response)


import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Loading... %{i+1}')
  bar.progress(i + 1)
  time.sleep(0.01)

'...and now we\'re done!'
