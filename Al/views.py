from django.shortcuts import render, redirect
from django.http import HttpResponse
from gtts import gTTS
import tempfile
import os

def speak_hindi(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')

        if not input_text:
            return HttpResponse('No text provided', status=400)

        try:
            # Initialize gTTS to convert English text to Hindi speech
            tts = gTTS(text=input_text, lang='hi')

            # Create a temporary file to save the output as an mp3
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                temp_filename = tmp_file.name
                tts.save(temp_filename)  # Save the file

            # Once saved, read the file and serve it
            with open(temp_filename, 'rb') as f:
                response = HttpResponse(f.read(), content_type="audio/mpeg")
                response['Content-Disposition'] = 'attachment; filename="output.mp3"'

            # Clean up the temporary file after the response is sent
            os.unlink(temp_filename)

            # After serving the response, redirect to clear the form
            return response
        except Exception as e:
            return HttpResponse(f'Error: {e}', status=500)

    # Render the input form if GET request or after redirect
    return render(request, 'speach.html')
