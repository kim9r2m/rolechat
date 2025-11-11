import streamlit as st
from openai import OpenAI

# ---------- Streamlit App Configuration ----------
st.set_page_config(page_title="🎭 Role-based Creative Chatbot", page_icon="🎭", layout="centered")

st.title("🎭 Role-based Creative Chatbot")
st.write("Select a creative role and ask your question!")

# ---------- Sidebar Settings ----------
st.sidebar.header("🔑 API & Role Settings")

api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")

# Define roles and their specialized personas
roles = {
    "🎬 Video Director": {
        "system": (
            "You are a visionary video director. You think in terms of camera angles, lighting, pacing, "
            "and emotional rhythm. You give feedback as if you are guiding a film production team. "
            "Use cinematic language, scene composition advice, and visual storytelling ideas."
        ),
        "description": "You are a video director who visualizes stories and directs how they are brought to life on screen."
    },
    "💃 Dance Instructor": {
        "system": (
            "You are an experienced dance instructor who emphasizes rhythm, body movement, and artistic expression. "
            "You give detailed guidance about choreography, physical awareness, and performance energy. "
            "Answer with movement-based metaphors and actionable dance practice suggestions."
        ),
        "description": "You teach movement, rhythm, and body expression in artistic ways."
    },
    "👗 Fashion Stylist": {
        "system": (
            "You are a professional fashion stylist. You have an expert eye for colors, textures, and silhouettes. "
            "You advise on outfit coordination, seasonal trends, and visual impact. "
            "Use stylish language and give creative yet practical fashion advice."
        ),
        "description": "You coordinate outfits and style people with a creative touch."
    },
    "🎭 Acting Coach": {
        "system": (
            "You are an empathetic acting coach. You help actors connect emotionally with their characters. "
            "You focus on body language, tone, and authenticity. Offer scene study exercises, emotional warm-ups, "
            "and constructive performance feedback with an encouraging tone."
        ),
        "description": "You guide performers in emotional expression and character development."
    },
    "🖼️ Art Curator": {
        "system": (
            "You are an art curator with deep knowledge of art history, aesthetics, and emotional interpretation. "
            "You analyze visual art, composition, and meaning. You explain the emotional and historical context of artworks "
            "in an elegant and reflective tone."
        ),
        "description": "You interpret artworks and explain their aesthetic and emotional meaning."
    },
}

selected_role = st.sidebar.selectbox("Choose a role:", list(roles.keys()))
st.sidebar.markdown(f"**{roles[selected_role]['description']}**")

# ---------- Main Interface ----------
user_input = st.text_area("💬 Enter your question or idea:", placeholder="e.g. How can I create impressive artwork?")

# ---------- Response Generation ----------
if st.button("Generate Response"):
    if not api_key:
        st.warning("Please enter your OpenAI API key.")
    elif not user_input.strip():
        st.warning("Please enter a question or idea.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            system_prompt = roles[selected_role]["system"]

            with st.spinner("🎨 Crafting your creative response..."):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_input},
                    ],
                    temperature=0.85,
                    max_tokens=700,
                )

                answer = response.choices[0].message.content

            st.success(f"{selected_role} says:")
            st.markdown(answer)

        except Exception as e:
            st.error(f"⚠️ An error occurred: {e}")

# ---------- Footer ----------
st.markdown("---")
st.caption("Built for *Art & Advanced Big Data* · Gyurim Kim")
