import streamlit as st
import random
import string
import re
from streamlit.components.v1 import html


def check_password_strength(password):        
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):  
        strength += 1
    if re.search(r'[a-z]', password):  
        strength += 1
    if re.search(r'[0-9]', password):  
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  
        strength += 1
    
    return strength


def password_strength_level(strength):
    if strength == 5:
        return "💪Very Strong"
    elif strength == 4:
        return "👍Strong"
    elif strength == 3:
        return "✅Moderate"
    elif strength == 2:
        return "⚠Weak"
    else:
        return "❌Very Weak"


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


st.markdown("""
    <style>
        .header {
            background-color: lightgray;
            color: black;
            padding: 10px;
            text-align: center;
            font-size: 24px;
        }
    </style>
    <div class="header">THE PROJECT OF GIAIC</div>
""", unsafe_allow_html=True)

st.title('Password Strength Meter & Generator')


with st.sidebar:
    st.header("Password Generator")
    password_length = st.slider("Select password length", min_value=8, max_value=20, value=12)
    generate_button = st.button("Generate Password")
    
    if generate_button:
        generated_password = generate_password(password_length)
        st.text_area("Generated Password", value=generated_password, height=100)


st.subheader('Password Strength Tester')


password = st.text_input('Enter Password to Test Strength', type="password")


if st.button("Check Strength"):
    if password:
        strength = check_password_strength(password)
        st.write(f"Password Strength: {password_strength_level(strength)}")
        
        
        strength_percentage = (strength * 20)
        st.progress(strength_percentage)
        st.write(f"Strength: {strength_percentage}%")
    else:
        st.warning("Please enter a password to check its strength.")




st.subheader('Password Strength Examples')
st.write("""
    **Very Weak**: `12345`
    
    **Weak**: `password`
    
    **Moderate**: `password123`
    
    **Strong**: `Passw0rd!23`
    
    **Very Strong**: `P@ssw0rd!$2023`
""")

st.title("")

st.write("💟This apps authorize, safe and secure app don't worry share any password")


footer = """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #D3D3D3;
        text-align: center;
        padding: 10px;
        font-size: 16px;
    }
    </style>
    <div class="footer">
        <p>Created by Engr M.Kamil Hanif | mkamilhanif789@gmail.com</p>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)

