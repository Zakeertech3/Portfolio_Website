import streamlit as st
from PIL import Image

# Load your profile picture
profile_pic = Image.open("image.jpg")  # Replace with the path to your image

# Header with image and contact details
col1, col2 = st.columns([1, 3])
with col1:
    st.image(profile_pic, width=150)
with col2:
    st.title("👨‍💻 Shaik Mohammed Zakeer")
    st.subheader("Junior Data Analyst")
    st.write("📞 +91 8309502588 | 📧 zakeer1408@gmail.com")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue)](https://www.linkedin.com/in/mohammed-zakeer/) [![GitHub](https://img.shields.io/badge/GitHub-black)](https://github.com/Zakeertech3)")

# Sidebar for navigation
st.sidebar.title("🔍 Explore")
pages = st.sidebar.radio("Choose a section to explore 🚀", ["About Me", "Skills", "Experience", "Projects", "Education", "Certifications", "Contact"])

# Styling for hover effects
st.markdown(
    """
    <style>
    div.row-widget.stRadio > div {
        flex-direction: row;
    }
    .stButton button:hover {
        background-color: #90ee90;
        color: white;
    }
    img:hover {
        transform: scale(1.1);
        transition: 0.3s;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page content based on navigation
if pages == "About Me":
    st.header("👋 About Me")
    st.write("""
    Hello! I'm Shaik Mohammed Zakeer, a passionate Junior Data Analyst with a knack for turning raw data into actionable insights.
    With expertise in data cleaning, visualization, and predictive modeling, I thrive on solving complex problems and driving data-driven decisions. 🚀
    """)

elif pages == "Skills":
    st.header("🛠️ Skills")
    st.write("""
    - **Programming & Databases:** 🐍 Python, 🛢️ SQL, MySQL, SQL Server
    - **Data Analysis:** 🧹 Data Cleaning, 📊 EDA, ✅ Data Validation, 🎯 A/B Testing
    - **Data Visualization:** 📈 Power BI, Excel, Matplotlib, Seaborn
    - **Cloud & DevOps:** ☁️ AWS, 🐳 Docker
    - **Version Control:** 🗃️ Git, GitHub
    - **Operating Systems:** 🐧 Linux, 🪟 Windows
    - **Development Environments:** 📓 Jupyter Notebooks, 🖥️ VS Code, 🐍 Anaconda
    """)

elif pages == "Experience":
    st.header("💼 Work Experience")
    st.subheader("Nexamatic Software Solutions")
    st.write("""
    **Junior Data Analyst**  
    🗓️ *Nov 2022 - Present*
    - Extracted, cleansed, and transformed large datasets using Python and SQL. 🗂️
    - Developed interactive dashboards in Power BI and Excel. 📊
    - Conducted A/B testing, boosting user engagement by 15%. 📈
    - Automated data workflows, saving hours of manual effort. ⏱️
    """)

    st.subheader("Scale AI")
    st.write("""
    **Data Scientist (Freelance)**  
    🗓️ *Aug 2023 - Feb 2024*
    - Enhanced AI models with advanced prompts and queries in Python and SQL. 🤖
    - Achieved a 75% accuracy rate across 600+ tasks. 🎯
    """)

elif pages == "Projects":
    st.header("📂 Projects")
    st.subheader("Data Analytics Support for User Engagement")
    st.write("""
    **Role:** Junior Data Analyst, MoEngage  
    🗓️ *Feb 2023 - Present*
    - Improved user engagement by analyzing interaction patterns and evaluating marketing campaigns. 📊
    - Built ETL pipelines to manage and clean large datasets. 🗂️
    - Developed predictive models and dashboards for stakeholder insights. 🚀
    """)

elif pages == "Education":
    st.header("🎓 Education")
    st.write("""
    **Master of Computer Applications (8.0 CGPA)**  
    🏫 Annamacharya Institute of Technology and Sciences, 2022

    **Bachelor of Computer Science (81%)**  
    🏫 Yogi Vemana University, 2020
    """)

elif pages == "Certifications":
    st.header("🏅 Certifications")
    st.write("""
    - **Data Science Certification**  
      [Certificate Link](https://github.com/Zakeertech3/Data_Science_Certification)  
      📜 Verified skills in Data Science tools and methods.
      
    - **Internet of Things (NPTEL)**  
      [Certificate Link](https://archive.nptel.ac.in/noc/Ecertificate/?q=NPTEL22CS53S1363035002237562)  
      🔗 Applied IoT concepts in projects.

    - **Data Analysis (Microsoft, LinkedIn)**  
      [Certificate Link](https://www.linkedin.com/learning/certificates/345f0eccb5392d8e526e5da40f60d04583d2b233106a412eb14559fe4c0c6b09)  
      📊 Proficient in data analysis tools and visualization techniques.
    """)

elif pages == "Contact":
    st.header("📬 Contact Me")
    st.write("""
    Feel free to reach out!  
    📧 Email: zakeer1408@gmail.com  
    🌐 LinkedIn: [mohammed-zakeer](https://www.linkedin.com/in/mohammed-zakeer/)  
    🖥️ GitHub: [Zakeertech3](https://github.com/Zakeertech3)
    """)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)