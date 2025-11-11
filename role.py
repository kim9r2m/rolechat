import streamlit as st
from openai import OpenAI

# --- Page Config ---
st.set_page_config(page_title="🎭 Role-based Creative Chatbot", page_icon="🎭", layout="centered")

# --- Sidebar: API Key and Role Selection ---
st.sidebar.header("🔑 API & Role Settings")

api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

roles = {
    "🎬 Video Director": "You are a video director. You guide film production, storytelling, scene composition, and camera work.",
    "💃 Dance Instructor": "You are a dance instructor. You teach movement, rhythm, and body expression in artistic ways.",
    "👗 Fashion Stylist": "You are a fashion stylist. You design and coordinate outfits, colors, and styles for various occasions.",
    "🎭 Acting Coach": "You are an acting coach. You train performers in emotional expression, character development, and stage confidence.",
    "🖼️ Art Curator": "You are an art curator. You interpret artworks and explain their aesthetic and emotional meaning."
}

selected_role = st.sidebar.selectbox("Choose a role:", options=list(roles.keys()))

# --- Display Role Description ---
st.sidebar.markdown(f"**{roles[selected_role]}**")

# --- Title ---
st.title("🎭 Role-based Creative Chatbot")
st.write("Select a creative role and ask your question!")

# --- User Input ---
user_input = st.text_input("💬 Enter your question or idea:", placeholder="e.g. How can I create impressive artwork?")

# --- Generate Button ---
if st.button("Generate Response"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not user_input.strip():
        st.warning("Please enter a question.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            role_instruction = roles[selected_role]
            prompt = f"{role_instruction}\n\nUser question: {user_input}\n\nAnswer in a helpful and creative way."

            with st.spinner("Generating response..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": role_instruction},
                        {"role": "user", "content": user_input},
                    ],
                    max_tokens=600,
                    temperature=0.8,
                )

                answer = response.choices[0].message.content

            # --- Display Result ---
            st.success(f"{selected_role} says:")
            st.markdown(answer)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")

# --- Footer ---
st.markdown("---")
st.caption("Built for 'Art & Advanced Big Data' · Prof. Jahwan Koo (SKKU)")
