---

## 🔧 Windows Development Environment Setup

1. **Create a `.env` File**

   - Command:
     ```
     New-Item -Path . -Name ".env" -ItemType "File" -Force
     ```
   - Purpose: Stores sensitive information like API keys securely.

2. **Load Environment Variables in Python**

   - Install `python-dotenv`:
     ```
     pip install python-dotenv
     ```
   - Usage:
     ```python
     from dotenv import load_dotenv
     load_dotenv()
     ```
   - Purpose: Loads environment variables from the `.env` file into your Python application.

3. **Start a Python Virtual Environment**

   - Command:
     ```
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - Purpose: Creates and activates a virtual environment to manage project-specific dependencies.

4. **Override Execution Policy for Current Session**

   - Command:
     ```
     Set-ExecutionPolicy RemoteSigned -Scope Process
     ```
   - Purpose: Allows script execution in the current session without changing global settings.

5. **Add `.env` to `.gitignore`**
   - Commands:
     ```
     New-Item -Path . -Name ".gitignore" -ItemType "File" -Force
     Add-Content -Path .\.gitignore -Value ".env"
     ```
   - Purpose: Prevents the `.env` file from being tracked by Git, ensuring sensitive information is not exposed.

6. ```$envFile = Get-Content -Path .\.env ```
---
