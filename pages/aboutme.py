import streamlit as st

st.title("About John Lloyd 👦")



st.title("🖼️Self Gallery")


image_paths = ["./pic/me3.jpg", "./pic/me1.jpg", "./pic/me2.jpg"]


cols = st.columns(len(image_paths))

for col, image_path in zip(cols, image_paths):
    col.image(image_path)


st.header("👨‍🎓 John Lloyd J. Pedilo")

st.markdown("""
##### 👨‍👦‍👦 Family Members

* 🤱 Mother's Name: Alma Pedilo
* 👨 Father's Name: Rodney Pedilo
* 👧 Sister's Name: Faith Pedilo

### 🔎 Overview
""", unsafe_allow_html=True)

# Personal Information
st.header("Personal Information")
st.write("**Name:** JOHN LLOYD PEDILO")
st.write("**Age:** 21 years old")
st.write("**Education:** Currently studying at CARLOS HILADO MEMORIAL STATE UNIVERSITY")
st.write("**Year:** 3rd year Bachelor of Science in Information Systems Student")
st.write("**Location:** Barangay Guinhalaran Silay City")




import streamlit as st


images = [
    {"path": "./pic/us1.jpg", "caption": "Bonding over a group project."},
    {"path": "./pic/us2.jpg", "caption": "Celebrating a school event together."},
    {"path": "./pic/us3.jpg", "caption": "MY LOVE."}
]

st.title("🖼️ Gallery")

for image in images:
    st.image(image["path"], caption=image["caption"])

st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
        padding: 2em;
    }
    h1, h2 {
        color: #4CAF50;
    }
    .stText {
        font-size: 1.2em;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Footer or additional sections (optional)
st.write("### Thank you for visiting my profile!")
st.write("Feel free to connect and reach out if you share similar interests or have any questions.")