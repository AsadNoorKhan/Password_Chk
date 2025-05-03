# Password Strength Checker

🔐 **Password Strength Checker** is a simple web application built with [Streamlit](https://streamlit.io) to evaluate the strength of passwords based on various criteria.

This app checks the following password rules:
- Minimum length of **8 characters**
- Contains **uppercase and lowercase letters**
- Contains at least **one digit (0-9)**
- Contains at least **one special character** (e.g., `!@#$%^&*`)

It provides real-time feedback to help users create strong, secure passwords!

## Features:
- **Password Rules**: The app checks for length, number inclusion, special characters, and letter case.
- **Visual Feedback**: Displays password strength with a progress bar and gives color-coded feedback.
- **Suggestions**: If the password is weak or moderate, the app will provide suggestions on how to improve it.

## How to Run Locally:
To run this app locally, follow these steps:

### 1. Clone the repository:
    ```bash
    git clone https://github.com/AsadNoorKhan/Password_Strength_Chk.git
    cd Password_Strength_Chk
    ```

### 2. Create a virtual environment (recommended):
    ```bash
    python -m venv venv
    ```

### 3. Activate the virtual environment:
    - On **Windows**:
        ```bash
        venv\Scripts\activate
        ```
    - On **Mac/Linux**:
        ```bash
        source venv/bin/activate
        ```

### 4. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
### 5. Run The App
    ```bash
    streamlit run pass.py
    ``` 