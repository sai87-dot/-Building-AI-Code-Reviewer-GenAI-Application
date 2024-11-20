#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install streamlit openai


# In[2]:


import streamlit as st
import openai
import difflib


# **Backend Logic**

# In[3]:


# Function to send the code to the OpenAI API
def analyze_code(code):
    try:
        response = openai.Completion.create(
            engine="code-davinci-002",
            prompt=f"Analyze the following Python code for bugs and suggest fixes:\n{code}",
            max_tokens=1000
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return str(e)

# Function to highlight differences between original and fixed code
def highlight_differences(original, fixed):
    diff = difflib.unified_diff(
        original.splitlines(), fixed.splitlines(), lineterm=""
    )
    return "\n".join(diff)


# **Streamlit UI**

# In[4]:


# Streamlit code for UI
st.title("GenAI App - AI Code Reviewer")
st.subheader("Submit your Python code for review and get detailed feedback.")

# Code input area
code_input = st.text_area("Paste your Python code here", height=300)

# File uploader
uploaded_file = st.file_uploader("Or upload a .py file", type="py")

if st.button("Submit for Review"):
    if code_input or uploaded_file:
        code = code_input or uploaded_file.read().decode()
        analysis = analyze_code(code)
        st.subheader("Bug Report and Suggestions")
        st.text(analysis)

        # Simulate fixed code for demonstration
        fixed_code = "def example():\n    return 'Fixed Code!'"

        st.subheader("Fixed Code")
        st.code(fixed_code, language='python')

        st.subheader("Code Differences")
        differences = highlight_differences(code, fixed_code)
        st.text(differences)

        # Option to download the fixed code
        st.download_button(
            label="Download Fixed Code",
            data=fixed_code,
            file_name="fixed_code.py",
            mime="text/x-python"
        )
    else:
        st.error("Please provide code input or upload a file.")


# **Run The App**

# In[9]:


# Save the code into a file
with open("app.py", "w") as f:
    f.write("""streamlit run C:\ProgramData\anaconda3\new folder  anaconda\Lib\site-packages\ipykernel_launcher.py [ARGUMENTS]
2024-11-20 13:20:42.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.140 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.140 Session state does not function when running a script without `streamlit run`
2024-11-20 13:20:42.151 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.152 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.153 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.153 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2024-11-20 13:20:42.156 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.""")


# In[12]:


streamlit run app.py


# In[ ]:




