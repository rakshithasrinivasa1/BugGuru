import os
import sys
import openai
from dotenv import load_dotenv

# ✅ Step 1: Load the OpenAI API Key from .env
print("🔹 Loading environment variables...")
if not load_dotenv():
    print("⚠ .env file not found or failed to load!")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("❌ ERROR: OpenAI API Key not found! Check your .env file.")
    sys.exit(1)

# openai.api_key = api_key



# Use Together.ai as the API provider
openai.api_base = "https://api.together.xyz/v1"
openai.api_key = api_key;  # Replace with your actual API key


# ✅ Step 2: Read Python Code from a File
# ✅ Read Python Code from a File (Fix Encoding Issue)
def read_code(file_path):
    """Reads code from the given file using UTF-8 encoding."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # ✅ Specify encoding
            return file.read()
    except FileNotFoundError:
        print(f"❌ ERROR: File '{file_path}' not found!")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"❌ ERROR: Unable to read '{file_path}' due to encoding issues. Try saving it as UTF-8.")
        sys.exit(1)


# ✅ Step 3: Send Code to OpenAI for Fixing
def fix_code_with_ai(code):
    """Sends code to OpenAI GPT for debugging and returns the fixed version."""
    prompt = f"""
    Below is a Python code snippet that may contain bugs. 
    Please:
    1. Identify and fix any issues.
    2. Explain the fixes.

    Code:
    ```
    {code}
    ```

    Return output in this format:
    ```
    # Fixed Code:
    <fixed_code>

    # Explanation:
    <explanation>
    ```
    """

    try:
        response = openai.ChatCompletion.create(
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"❌ ERROR: OpenAI request failed - {e}")
        sys.exit(1)

# ✅ Step 4: Run the Bug Fixing Process
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ ERROR: No file provided!")
        print("Usage: python bug_fixer.py <your_python_file.py>")
        sys.exit(1)

    file_path = sys.argv[1]
    print(f"🔍 Reading code from: {file_path}")

    code = read_code(file_path)
    print("\n🛠 Sending code to OpenAI for bug fixing...\n")

    fixed_code = fix_code_with_ai(code)

    print("\n✨ AI Debugging Result:\n")
    print(fixed_code)

    # ✅ Step 5: Save Fixed Code
    output_file = f"fixed_{os.path.basename(file_path)}"
    with open(output_file, "w") as f:
        f.write(fixed_code.split("\n\n# Explanation:")[0].strip())

    print(f"\n✅ Fixed code saved to: {output_file}")
