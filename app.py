import os
import google.generativeai as genai
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

# --- CONFIGURATION ---
# Ensure your key is from https://aistudio.google.com/
API_KEY = "AIzaSyD03zdUugitrUO2SLCTONHrx2xLsRX8feU"

# Force 'rest' transport to avoid common local environment SSL/gRPC 404 errors
genai.configure(api_key=API_KEY, transport='rest')

# Using the 2026 Stable Workhorse
MODEL_NAME = 'gemini-2.5-flash' 
model = genai.GenerativeModel(MODEL_NAME)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file:
            return render_template('index.html', error="Please select an image first.")

        try:
            # Open the uploaded image
            img = Image.open(file.stream)
            
            # --- PROFESSIONAL BOTANICAL PROMPT ---
            # This prompt ensures high-detail output for your website
            prompt = """
            You are a professional botanist. Identify the plant in this image and provide:
            1. **Botanical Identity**: Common Name, Scientific Name, and Family.
            2. **Deep Care Guide**: 
               - Light: Specific hours and intensity (e.g., indirect vs direct).
               - Water: Detailed schedule for summer vs winter.
               - Soil: Ideal pH range and drainage components.
            3. **Growth Expectancy**: Typical height and growth rate.
            4. **Troubleshooting**: 2 common pests or diseases for this specific plant and how to treat them.
            5. **Pro Tip**: One secret to making this plant thrive.
            """
            
            # Generate content from Gemini
            response = model.generate_content([prompt, img])
            
            # response.text contains the full structured botanical profile
            return render_template('index.html', full_info=response.text)

        except Exception as e:
            return render_template('index.html', error=f"System Error: {str(e)}")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
