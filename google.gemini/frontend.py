import streamlit as st

st.set_page_config(
    page_title="EduGenie",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 EduGenie")
st.subheader("AI-Powered Educational Assistant")

st.write("Learn easily with smart answers, quizzes and learning paths.")

# -----------------------------
# Scenario 1: Question Answer
# -----------------------------

st.header("📚 Ask a Question")

question = st.text_input(
    "Enter your question:",
    placeholder="Which is the largest ocean?"
)

if st.button("Ask EduGenie"):
    if question:
        q = question.lower()

        if "largest ocean" in q:
            answer = "🌊 The Pacific Ocean is the largest ocean on Earth."
        elif "pythagoras" in q:
            answer = "📐 The Pythagorean Theorem states that a² + b² = c²."
        elif "sql" in q:
            answer = "💻 SQL is a language used to store, retrieve and manage data in databases."
        else:
            answer = "🤖 Please ask a specific academic question."

        st.success(answer)


# -----------------------------
# Scenario 2: Quiz
# -----------------------------

st.header("📝 Generate Quiz")

topic = st.selectbox(
    "Choose a topic:",
    ["Pythagoras Theorem", "SQL", "Python", "Machine Learning"]
)

if st.button("Generate Quiz"):
    if topic == "Pythagoras Theorem":
        questions = [
            "1. What is the Pythagorean Theorem?",
            "2. Which side is called the hypotenuse?",
            "3. When is the theorem used?",
            "4. If a = 3 and b = 4, what is c?",
            "5. What is the longest side of a right triangle?"
        ]

    elif topic == "SQL":
        questions = [
            "1. What is SQL?",
            "2. What is a database?",
            "3. What is SELECT used for?",
            "4. What is a primary key?",
            "5. What is a JOIN?"
        ]

    elif topic == "Python":
        questions = [
            "1. What is Python?",
            "2. What is a variable?",
            "3. What is a list?",
            "4. What is a function?",
            "5. What is a loop?"
        ]

    else:
        questions = [
            "1. What is Machine Learning?",
            "2. What is supervised learning?",
            "3. What is unsupervised learning?",
            "4. What is classification?",
            "5. What is clustering?"
        ]

    for q in questions:
        st.write(q)


# -----------------------------
# Scenario 3: Learning Path
# -----------------------------

st.header("🛣️ Personalized Learning Path")

learning_topic = st.selectbox(
    "Select learning topic:",
    ["SQL", "Python", "Machine Learning"]
)

if st.button("Create Learning Path"):

    if learning_topic == "SQL":

        st.subheader("SQL – 4 Week Learning Path")

        st.write("### 🟢 Beginner")
        st.write(
            "Database basics → Tables → SELECT → WHERE → ORDER BY"
        )

        st.write("### 🟡 Intermediate")
        st.write(
            "INSERT → UPDATE → DELETE → JOIN → GROUP BY → Subqueries"
        )

        st.write("### 🔴 Advanced")
        st.write(
            "Indexes → Views → Transactions → Normalization → Query Optimization"
        )

        st.info(
            "💡 Suggestion: Practice 5 SQL queries every day "
            "and build a small student database project."
        )

    elif learning_topic == "Python":

        st.subheader("Python – 4 Week Learning Path")

        st.write("### 🟢 Beginner")
        st.write("Variables → Data Types → Operators → Conditions → Loops")

        st.write("### 🟡 Intermediate")
        st.write("Functions → Lists → Tuples → Dictionaries → OOP")

        st.write("### 🔴 Advanced")
        st.write("Modules → Exception Handling → Files → Projects")

    else:

        st.subheader("Machine Learning – 4 Week Learning Path")

        st.write("### 🟢 Beginner")
        st.write("AI basics → ML basics → Data → Features → Labels")

        st.write("### 🟡 Intermediate")
        st.write("Classification → Regression → KNN → K-Means")

        st.write("### 🔴 Advanced")
        st.write("SVM → Neural Networks → Model Evaluation → Projects")


st.divider()

st.caption("EduGenie – Learn Smart. Learn Simple. 🎓")
