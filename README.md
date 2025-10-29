this is meaningless stuff done for some reasons. please do not waste your time here.

# 🦄 Muskito Chatbot

A dual-personality chatbot powered by Groq's LLM with two distinct modes:

1. **🌈 Happy & Delusional Mode**: Extremely happy, complementing, like a 15-year-old girl who loves unicorns
2. **🔥 Brutal Roaster Mode**: Keeps it real, ego crusher, brutally honest, realistically horrific

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Variables:**
   Create a `.env` file in the root directory and add your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## How It Works

Muskito uses **system prompts** to achieve different personalities. This approach:
- ✅ No fine-tuning required
- ✅ Easy to switch between modes instantly
- ✅ Adjustable prompts for quick iteration
- ✅ Works with any compatible LLM

The system prompts define the personality, tone, and behavior patterns for each mode, allowing the same LLM to behave completely differently based on the selected mode.

## Usage

1. Launch the app using `streamlit run app.py`
2. Select your desired mode using the radio buttons
3. Start chatting! The chatbot will respond according to the selected personality
4. Switch modes anytime - the chat history will be cleared when switching

## File Structure

- `muskito.py` - Core Muskito chatbot class with Groq integration and personality modes
- `app.py` - Streamlit UI application
- `requirements.txt` - Python dependencies
- `.env` - Environment variables (create this file)

