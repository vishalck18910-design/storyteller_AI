
import streamlit as st

from story import generate_story


# ----------------------------------
# 1. PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📖",
    layout="centered"
)


# ----------------------------------
# 2. APPLICATION TITLE
# ----------------------------------

st.title("📖 AI Story Generator")

st.write(
    "Create your own stories using Artificial Intelligence."
)


# ----------------------------------
# 3. START BUTTON
# ----------------------------------

if "started" not in st.session_state:
    st.session_state.started = False

if st.button("🚀 Start", use_container_width=True):
    st.session_state.started = True


# ----------------------------------
# 4. USER INPUT SECTION
# ----------------------------------

if st.session_state.started:

    st.subheader("Create Your Story")

    topic = st.text_input(
        "Enter your story topic",
        placeholder="Example: A missing scientist..."
    )

    genre = st.selectbox(
        "Select Story Genre",
        ["Thriller", "Comedy", "Fiction"]
    )

    length = st.selectbox(
        "Select Story Length",
        ["Brief", "Medium", "Full Length"]
    )


    # ----------------------------------
    # 5. GENERATE STORY BUTTON
    # ----------------------------------

    if st.button("✨ Generate Story", use_container_width=True):

        if not topic.strip():

            st.warning("Please enter a story topic.")

        else:

            with st.spinner("Your story is being generated..."):

                try:

                    story = generate_story(
                        topic,
                        genre,
                        length
                    )

                    st.success("Your story has been generated!")

                    st.subheader("📚 Your Generated Story")

                    st.markdown(story)

                except Exception as e:

                    st.error(f"Something went wrong: {e}")


# ----------------------------------
# 6. FOOTER
# ----------------------------------

st.divider()

st.caption("Powered by Python, Streamlit and Groq AI")
