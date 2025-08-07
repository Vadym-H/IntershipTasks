import google.generativeai as genai
import os
import argparse
from dotenv import load_dotenv

def describe_image(image_path: str) -> str:
    """Generate a brief description of the image."""
    prompt = """Provide a clear, concise description of this image in 2-3 short sentences. 
    Focus on the main subject and key details. Use plain text only, no markdown formatting."""
    
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    try:
        with open(image_path, 'rb') as img_file:
            response = model.generate_content([
                prompt,
                {"mime_type": "image/png", 
                 "data": img_file.read()}
            ])
        return response.text.strip()
    except Exception as e:
        return f"Error processing image: {str(e)}"

def translate_to_spanish(text: str) -> str:
    """Translate the given text to Spanish."""
    model = genai.GenerativeModel('gemini-2.5-flash')
    try:
        response = model.generate_content(
            f"Translate the following English text to Spanish. Return only the translation, no additional text.\n\n{text}"
        )
        return response.text.strip()
    except Exception as e:
        return f"Translation error: {str(e)}"

def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables")
        return
        
    genai.configure(api_key=api_key)
    
    parser = argparse.ArgumentParser(description='Describe and translate image content')
    parser.add_argument('image_path', nargs='?', help='Path to the image file')
    args = parser.parse_args()
    
    image_path = args.image_path
    if not image_path:
        image_path = input("Enter the path to the image file: ").strip('"')
    
    if not os.path.exists(image_path):
        print(f"Error: File not found: {image_path}")
        return
    
    print("\nGenerating description...\n")
    
    # Get and display English description
    description = describe_image(image_path)
    print("English Description:")
    print("-" * 30)
    print(description)
    
    # Get and display Spanish translation
    print("\nSpanish Translation:")
    print("-" * 30)
    translation = translate_to_spanish(description)
    print(translation)

if __name__ == "__main__":
    main()