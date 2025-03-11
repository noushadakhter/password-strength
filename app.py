import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include at least one number (0-9).")
    
    if re.search(r"[!@#$%^&-_*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&-_*).")
    
    common_passwords = ["password123", "12345678", "qwerty", "abc123", "password1"]
    if password in common_passwords:
        score = 1  # Reset score to weak
        feedback = ["❌ This password is too common. Choose a more unique password."]
    
    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return strength, feedback

def generate_strong_password():
    characters = string.ascii_letters + string.digits + "!@#$%^&-_*"
    return ''.join(random.choice(characters) for _ in range(12))

def apply_custom_css():
    st.markdown("""
        <style>
            .stApp {
                max-width: 500px;
                margin: auto;
                padding: 30px;
                border-radius: 10px;
                background: white;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            .stTextInput>div>div>input {
                border-radius: 8px;
                border: 1px solid #ccc;
                padding: 12px;
                width: 100%;
            }
            .stButton>button {
                background-color: #007BFF;
                color: white;
                border-radius: 8px;
                padding: 12px 20px;
                border: none;
                font-size: 16px;
                width: 100%;
            }
            .stButton>button:hover {
                background-color: #0056b3;
            }
            .feedback-box {
                background-color: #f8d7da;
                color: #721c24;
                padding: 10px;
                border-radius: 5px;
                margin-top: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

def main():
    apply_custom_css()
    st.title("🔐 Password Strength Meter")
    st.write("Enter your password below to check its security level. 🔍")
    
    password = st.text_input("Enter your password:", type="password")
    
    if st.button("Check Strength"):
        if password:
            strength, feedback = check_password_strength(password)
            st.subheader(f"🛡 Password Strength: {strength}")
            if feedback:
                st.markdown("""<div class='feedback-box'>""" + "<br>".join(feedback) + "</div>", unsafe_allow_html=True)
            else:
                st.success("✅ Your password is strong!")
        else:
            st.error("⚠ Please enter a password.")
    
    if st.button("🔑 Generate Strong Password"):
        strong_password = generate_strong_password()
        st.text(f"Suggested Password: {strong_password}")

if __name__ == "__main__":
    main()


#footer
st.write("- - -")
st.write("Keep believing in yourself🍀")
st.write("**Created by Noushad Akhter**")
