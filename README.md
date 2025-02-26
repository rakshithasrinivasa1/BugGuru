# BugGuru
BugGuru 🧑‍💻🔍 – Your AI-powered debugging expert! It not only automatically detects and fixes code bugs but also explains the fixes to help you write better code. 


## 📌 Overview
BugGuru is an AI-driven debugging and test-generation tool designed to help developers **identify, fix, and optimize Python code** efficiently. It leverages **OpenAI's Llama models via Together.ai** to detect bugs, provide AI-generated fixes, optimize performance, and generate test cases. It includes a **live debugging mode** for real-time insights and an optional **VS Code extension** for seamless integration.

---

## 🚀 Features
- **Bug Detection & Fixing:** AI identifies and corrects Python code errors.
- **Code Optimization:** Suggests performance improvements.
- **Test Generation:** Auto-generates unit test cases.
- **Live Debugging:** Provides real-time AI insights while coding.
- **VS Code Extension:** Allows easy debugging and test generation.

---

## 🛠 Setup & Installation
### **1. Clone the Repository**
```bash
git clone https://github.com/rakshithasrinivasa1/BugGuru.git
cd BugGuru
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up API Key**
- Create a `.env` file in the root directory.
- Add your Together.ai API key:
```env
OPENAI_API_KEY=your_api_key_here
```

---

## ⚡ Usage
### **1. Run Bug Detection & Fixing**
```bash
python bug_fixer.py buggy_script.py
```

### **2. Optimize Code**
```bash
python code_optimizer.py performance_script.py
```

### **3. Generate Test Cases**
```bash
python test_generator.py function_script.py
```

### **4. Live Debugging Mode**
```bash
python live_debugger.py script.py
```

### **5. Use CLI Tool (Main Entry Point)**
(Note: script.py is just an example file for testing purposes.)
```bash
python main.py fix script.py
python main.py optimize script.py
python main.py test script.py
python main.py debug script.py
```

---

## 📌 VS Code Extension (Optional)
To integrate BugGuru++ into VS Code:
1. Install **Node.js & npm**
2. Run:
```bash
npx @vscode/create-extension
```
3. Modify `package.json` to execute `main.py` commands.
4. Load the extension into VS Code.

---

## 🔒 Security & Privacy
- **No local storage of code** – AI interactions are transient.
- **API key protection** – Store credentials in `.env` file.
- **User control** – Option to disable AI suggestions.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 👥 Contributors
- Rakshitha Srinivasa  
- email-rakshithasrinivasa111@gmail.com

---

## 🛠 Future Improvements
- Support for additional programming languages.
- Cloud-based AI debugging dashboard.
- Enhanced AI-powered code reviews.

---

## 📩 Contact
For issues or suggestions, create a GitHub issue or reach out via email: **rakshithasrinivasa111@gmail.com**.

---




