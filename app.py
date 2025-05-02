import streamlit as st
import pandas as pd
import time
import pyautogui
import webbrowser
import os

st.set_page_config(page_title="WhatsApp Bulk Sender", layout="centered")

st.title("📤 WhatsApp Message Sender using Automation")
st.markdown("Upload your Excel file and enter the message you want to send to all contacts via WhatsApp Web.")

uploaded_file = st.file_uploader("📁 Upload Excel File (.xlsx)", type=["xlsx"])
custom_message = st.text_area("💬 Enter your message here:", height=100)

start_button = st.button("🚀 Send Messages")

def send_whatsapp_messages(df, message):
    df.columns = df.columns.str.strip()
    webbrowser.open("https://web.whatsapp.com")
    st.info("Please scan the QR code manually in the browser. Waiting for 25 seconds...")
    time.sleep(25)

    for index, row in df.iterrows():
        name = str(row['Name']).strip()
        phone = str(row['Phone Number']).strip()

        if not phone.startswith('+'):
            phone = '+91' + phone

        st.write(f"📤 Sending message to **{name} ({phone})**")

        pyautogui.click(250, 200)  # Adjust if needed
        time.sleep(1)
        pyautogui.typewrite(phone)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.typewrite(message)
        time.sleep(1)
        pyautogui.press("enter")
        st.success(f"✅ Message sent to {name}!")

        time.sleep(2)

    os.system("taskkill /im chrome.exe /f")
    st.success("✅ All messages sent and browser closed.")

if start_button:
    if uploaded_file is not None and custom_message.strip() != "":
        try:
            df = pd.read_excel(uploaded_file)
            send_whatsapp_messages(df, custom_message)
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("Please upload a file and enter a message.")
