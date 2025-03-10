#
import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

st.title("🔒 Password Generator 🗝️")

# Adjusted max_value to allow for longer passwords
length = st.slider("Select password length", min_value=4, max_value=20, value=12)

use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.success(f"🔒 Your generated password is: **{password}**")

st.write("---")

st.write("Made with ❤️ by [Maheen Ghouri 😄😎🕶]")

# Optional: Background image (replace with your image URL)
background_image = """
<style>
.stApp {
    background-image: url("https://www.google.com/imgres?q=programing%20wallpaper%20for%20pc&imgurl=https%3A%2F%2Fimg.freepik.com%2Ffree-photo%2Fhtml-css-collage-concept_23-2150061955.jpg&imgrefurl=https%3A%2F%2Fwww.freepik.com%2Ffree-photos-vectors%2Fcomputer-programming&docid=yF94OMXEmJ_sPM&tbnid=Vq5ZpNgnh09RYM&vet=12ahUKEwjDqMnj6P-LAxXhKvsDHTWzPMA4ChAzegQIGhAA..i&w=626&h=418&hcb=2&ved=2ahUKEwjDqMnj6P-LAxXhKvsDHTWzPMA4ChAzegQIGhAA");
    background-size: cover;
    background-position: center;
}
</style>
"""

#st.markdown(background_image, unsafe_allow_html=True)