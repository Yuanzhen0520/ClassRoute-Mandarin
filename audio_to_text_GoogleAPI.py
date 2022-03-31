def transcribe_model_selection(speech_file, model,f):
    
    from google.cloud import speech

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-US",
        model=model,
        audio_channel_count=2,
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)

    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print("First alternative of result {}".format(i))
        print(u"Transcript: {}".format(alternative.transcript))
        f.write(alternative.transcript)

with open('/Users/zc/Documents/GitHub/ClassRoute/py/Code/audio/Permutation/output.txt','w',encoding='utf-8') as f: #write the output as txt
    for i in range(0,12):
        path="/Users/zc/Documents/GitHub/ClassRoute/py/Code/audio/Permutation/output-{0}.wav".format(i)
        transcribe_model_selection(path,"video",f)
