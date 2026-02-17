# # # # from flask import Flask, render_template, request
# # # # from google import genai
# # # # import PIL.Image
# # # # import io
# # # # import time

# # # # app = Flask(__name__)

# # # # # --- CONFIGURATION ---
# # # # # Replace with a fresh key from https://aistudio.google.com/
# # # # GEMINI_KEY = "AIzaSyBhsF2ISBwBmlXYrItZUCzHb-qw9LQ4upY"
# # # # client = genai.Client(api_key=GEMINI_KEY)

# # # # def prepare_image(file_storage):
# # # #     """Compresses image to prevent SSL/Timeout errors."""
# # # #     img = PIL.Image.open(file_storage.stream)
# # # #     # Convert to RGB if necessary (handles PNGs with transparency)
# # # #     if img.mode in ("RGBA", "P"):
# # # #         img = img.convert("RGB")
    
# # # #     # Resize if very large to save bandwidth/quota
# # # #     img.thumbnail((1024, 1024)) 
# # # #     return img

# # # # @app.route('/', methods=['GET', 'POST'])
# # # # def index():
# # # #     if request.method == 'POST':
# # # #         file = request.files.get('file')
        
# # # #         if file:
# # # #             try:
# # # #                 # 1. Prepare and Compress Image
# # # #                 img = prepare_image(file)
                
# # # #                 prompt = "Identify this plant and give 3 short, easy care tips."
                
# # # #                 # 2. Retry Logic for unstable connections
# # # #                 for attempt in range(2):
# # # #                     try:
# # # #                         response = client.models.generate_content(
# # # #                             model="gemini-2.0-flash",
# # # #                             contents=[prompt, img]
# # # #                         )
# # # #                         return render_template('index.html', full_info=response.text)
# # # #                     except Exception as conn_err:
# # # #                         if attempt == 0: 
# # # #                             time.sleep(2) # Wait 2 seconds and try again
# # # #                             continue
# # # #                         raise conn_err
            
# # # #             except Exception as e:
# # # #                 error_str = str(e)
# # # #                 # Friendly error messages for common problems
# # # #                 if "429" in error_str:
# # # #                     msg = "Quota exceeded. Please wait 1 minute."
# # # #                 elif "EOF" in error_str or "SSL" in error_str:
# # # #                     msg = "Connection dropped. Try a smaller photo or better Wi-Fi."
# # # #                 elif "API key not valid" in error_str:
# # # #                     msg = "Invalid API Key. Please update it in app.py."
# # # #                 else:
# # # #                     msg = f"Error: {error_str}"
                
# # # #                 return render_template('index.html', error=msg)

# # # #     return render_template('index.html')

# # # # if __name__ == '__main__':
# # # #     app.run(debug=True)





# 2
# # # from flask import Flask, render_template, request
# # # from google import genai
# # # import PIL.Image
# # # import io
# # # import time

# # # app = Flask(__name__)

# # # # --- CONFIGURATION ---
# # # # Replace with a fresh key from https://aistudio.google.com/
# # # GEMINI_KEY = "AIzaSyB2N24Z8JE2pvstLA1pgL3K22Z_HgT8dgo"
# # # client = genai.Client(api_key=GEMINI_KEY)

# # # def prepare_and_compress_image(file_storage):
# # #     """
# # #     Opens, converts to RGB, and resizes the image to 800x800.
# # #     This significantly reduces 'token' usage and prevents SSL timeouts.
# # #     """
# # #     img = PIL.Image.open(file_storage.stream)
    
# # #     # Convert to RGB (required for JPEGs and handles PNG transparency)
# # #     if img.mode in ("RGBA", "P"):
# # #         img = img.convert("RGB")
    
# # #     # Resize to 800x800 to save your quota (as requested)
# # #     img.thumbnail((800, 800)) 
# # #     return img

# # # @app.route('/', methods=['GET', 'POST'])
# # # def index():
# # #     if request.method == 'POST':
# # #         file = request.files.get('file')
        
# # #         if file:
# # #             try:
# # #                 # 1. Prepare and Compress Image using the new logic
# # #                 img = prepare_and_compress_image(file)
                
# # #                 prompt = "Identify this plant and give 3 short, easy care tips."
                
# # #                 # 2. Retry Logic for unstable connections
# # #                 for attempt in range(2):
# # #                     try:
# # #                         response = client.models.generate_content(
# # #                             model="gemini-2.0-flash",
# # #                             contents=[prompt, img]
# # #                         )
# # #                         return render_template('index.html', full_info=response.text)
# # #                     except Exception as conn_err:
# # #                         if attempt == 0: 
# # #                             time.sleep(2) # Wait 2 seconds and try again
# # #                             continue
# # #                         raise conn_err
            
# # #             except Exception as e:
# # #                 error_str = str(e)
# # #                 # Friendly error messages for common problems
# # #                 if "429" in error_str:
# # #                     msg = "Quota exceeded. Please wait 1 minute."
# # #                 elif "EOF" in error_str or "SSL" in error_str:
# # #                     msg = "Connection dropped. Try a smaller photo or better Wi-Fi."
# # #                 elif "API key not valid" in error_str:
# # #                     msg = "Invalid API Key. Please update it in app.py."
# # #                 else:
# # #                     msg = f"Error: {error_str}"
                
# # #                 return render_template('index.html', error=msg)

# # #     return render_template('index.html')

# # # if __name__ == '__main__':
# # #     app.run(debug=True)



# 3
# # from flask import Flask, render_template, request
# # from google import genai
# # import PIL.Image
# # import time

# # app = Flask(__name__)

# # # --- CONFIGURATION ---
# # # Ensure there is no extra 'A' at the start!
# # GEMINI_KEY = "AIzaSyDjFyVei17p_sCLPLkVDgX4TDMEp5kxHo0"
# # client = genai.Client(api_key=GEMINI_KEY)

# # # Global variable to track time and save quota
# # last_request_time = 0

# # def prepare_and_compress_image(file_storage):
# #     """Resizes to 800px to use minimum possible tokens."""
# #     img = PIL.Image.open(file_storage.stream)
# #     if img.mode in ("RGBA", "P"):
# #         img = img.convert("RGB")
# #     img.thumbnail((800, 800)) 
# #     return img

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     global last_request_time
    
# #     if request.method == 'POST':
# #         # 1. Local Limit Check: Prevent requests more than once every 20 seconds
# #         current_time = time.time()
# #         if current_time - last_request_time < 20:
# #             wait_time = int(20 - (current_time - last_request_time))
# #             return render_template('index.html', error=f"Please wait {wait_time} seconds before the next analysis.")

# #         file = request.files.get('file')
# #         if file:
# #             try:
# #                 last_request_time = time.time() # Update time ONLY when request starts
# #                 img = prepare_and_compress_image(file)
# #                 prompt = "Identify this plant and give 3 short, easy care tips."
                
# #                 response = client.models.generate_content(
# #                     model="gemini-2.0-flash",
# #                     contents=[prompt, img]
# #                 )
# #                 return render_template('index.html', full_info=response.text)
            
# #             except Exception as e:
# #                 error_str = str(e)
# #                 if "429" in error_str:
# #                     msg = "Google Quota Full. You have reached the 1,500 daily limit. Try again tomorrow."
# #                 else:
# #                     msg = f"Error: {error_str}"
# #                 return render_template('index.html', error=msg)

# #     return render_template('index.html')

# # if __name__ == '__main__':
# #     app.run(debug=True)






# 4
# import os
# import google.generativeai as genai
# from flask import Flask, render_template, request
# from PIL import Image

# app = Flask(__name__)

# # --- CONFIGURATION ---
# # Replace with your actual key from https://aistudio.google.com/
# API_KEY = "AIzaSyD499og676FHLF0rJYyjHuomsK2W8ZdXSg"

# # 1. Force use of v1 (Stable) to avoid 'v1beta' 404 errors
# genai.configure(api_key=API_KEY, transport='rest')

# # 2. Use the STABLE alias for 2026
# MODEL_NAME = 'gemini-2.5-flash' 
# model = genai.GenerativeModel(MODEL_NAME)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         file = request.files.get('file')
#         if not file:
#             return render_template('index.html', error="Please select an image first.")

#         try:
#             # Open the uploaded image
#             img = Image.open(file.stream)
            
#             # Request identification and care tips
#             prompt = "Identify this plant and give 3 tiny care tips (Sun, Water, Soil)."
            
#             # Generate content
#             response = model.generate_content([prompt, img])
            
#             return render_template('index.html', full_info=response.text)

#         except Exception as e:
#             # If 404 persists, this will help us see if the API key is restricted
#             return render_template('index.html', error=f"API Error: {str(e)}")

#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)



import os
import google.generativeai as genai
from flask import Flask, render_template, request
from PIL import Image

app = Flask(__name__)

# --- CONFIGURATION ---
# Ensure your key is from https://aistudio.google.com/
API_KEY = "AIzaSyD499og676FHLF0rJYyjHuomsK2W8ZdXSg"

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