import streamlit as st

st.set_page_config(page_title='Python', layout='wide',
                #    initial_sidebar_state=st.session_state.get('sidebar_state', 'collapsed'),
)

st.header("Python - CheatSheet")

_, exp_col, _ = st.columns([1,3,1])
with exp_col:
    with st.expander("**📖 How to use this CheatSheet?**"):
        st.markdown("""

                    The Python cheat sheet is a one-page reference sheet for the Python 3 programming language.

                    A popular programming language. Python can be used on a server to create web applications.
                    """)
        
        st.info("""
                This application is only secondary to the official Python documentation and serves as a quick guide through code snippets to learn Python. Offical documentation [here.](https://www.python.org/)
                """)

st.sidebar.title("Python Cheatsheet 📄")

sections = {
    "Home": "Welcome to the Home page! Here is some introduction content.",
    "About": "This is the About section. Here we provide information about our project.",
    "Services": "In the Services section, we describe the services we offer.",
    "Contact": "This is the Contact section. Feel free to reach out to us!"
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(sections.keys()))

# Function to display the selected section content
def display_section(section_name):
    st.title(section_name)
    st.write(sections[section_name])
    if section_name == "Home":
        st.write("Additional content for the Home page.")
    elif section_name == "About":
        st.write("Detailed information about the project.")
    elif section_name == "Services":
        st.write("Descriptions of the services you offer.")
    elif section_name == "Contact":
        st.write("Contact form or contact information.")
        contact_form = """
        <form action="https://formspree.io/your-email@domain.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="_replyto" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message"></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

# Display all sections but highlight the selected one
for section in sections:
    if section == selection:
        display_section(section)
        st.write("---")  # Separator between sections
    else:
        st.write(f"### {section}")
        st.write(f"[Jump to {section}](#{section.replace(' ', '-').lower()})")

# Add a back-to-top link at the end of each section
st.write("### Back to top")
st.write("[Go to Home](#home)")

cols = st.columns(2)