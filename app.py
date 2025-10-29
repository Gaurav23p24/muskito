"""
Streamlit UI for Muskito Chatbot
"""
import streamlit as st
from muskito import Muskito

# Page configuration
st.set_page_config(
    page_title="Muskito Chatbot",
    page_icon="🦄",
    layout="wide"
)

# Initialize session state
if "muskito" not in st.session_state:
    st.session_state.muskito = Muskito()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_mode" not in st.session_state:
    st.session_state.current_mode = "happy_delusional"

# Title and mode selector
st.title("🦄 Muskito Chatbot")
st.markdown("---")

# Mode selector with visual styling
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    mode_selection = st.radio(
        "Choose Muskito's Personality:",
        options=["happy_delusional", "brutal_roaster"],
        format_func=lambda x: "🌈 Happy & Delusional" if x == "happy_delusional" else "🔥 Brutal Roaster",
        horizontal=True,
        index=0 if st.session_state.current_mode == "happy_delusional" else 1
    )

# Update mode if changed
if mode_selection != st.session_state.current_mode:
    st.session_state.current_mode = mode_selection
    st.session_state.muskito.set_mode(mode_selection)
    # Clear messages when switching modes for a fresh start
    st.session_state.messages = []
    st.session_state.muskito.clear_history()
    st.rerun()

# Display mode info
if st.session_state.current_mode == "happy_delusional":
    st.info("🌈 **Current Mode: Happy & Delusional** - Muskito is in unicorn-loving, compliment-giving mode!")
else:
    st.warning("🔥 **Current Mode: Brutal Roaster** - Muskito is ready to keep it 100% real (brutally honest)!")

st.markdown("---")

# Chat interface
st.subheader("Chat with Muskito")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get response from Muskito
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Stream the response
        for chunk in st.session_state.muskito.chat(prompt, stream=True):
            full_response += chunk
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to messages
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with controls
with st.sidebar:
    st.header("⚙️ Controls")
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.muskito.clear_history()
        st.rerun()
    
    st.markdown("---")
    st.markdown("### About Muskito")
    st.markdown("""
    **Muskito** is a chatbot with dual personalities:
    
    - 🌈 **Happy & Delusional**: Extremely positive, 
      complimentary, unicorn-loving mode
    
    - 🔥 **Brutal Roaster**: No-nonsense, ego-crushing,
      brutally honest mode
    
    Switch between modes using the radio buttons above!
    """)

