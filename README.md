# 🎯 Adaptive Learning System (OpenEnv)

## 🚀 Overview

This project implements an **adaptive learning environment** where an intelligent agent dynamically selects learning actions (videos, exercises, quizzes, etc.) based on the student’s current state.

Unlike static learning flows, this system **continuously adapts** using feedback such as:

* Concept mastery
* Fatigue level
* Learning attempts
* Engagement

---

## 🧠 Key Features

### ✅ Adaptive Decision Making

* Chooses actions based on real-time student state
* Avoids fixed or repetitive learning sequences

### 🎲 Exploration Mechanism

* Introduces controlled randomness to prevent deterministic behavior
* Ensures diverse learning paths across runs

### 🔁 Anti-Repetition Logic

* Prevents looping actions (e.g., repeated quizzes or exercises)

### 📊 Reward-Driven System

* Rewards meaningful learning progress
* Penalizes ineffective actions (e.g., premature quizzes, low engagement)

### 🧩 Realistic Learning Simulation

* Models fatigue and engagement
* Simulates gradual concept mastery

---

## ⚙️ Tech Stack

* Python 3.10
* Docker (containerized execution)
* OpenEnv framework

---

## 📁 Project Structure

```id="j1n9h4"
.
├── agents/
│   └── baseline_agent.py      # Adaptive agent logic
├── env/
│   ├── learning_env.py        # Environment + reward logic
│   └── openenv_wrapper.py     # Wrapper integration
├── inference.py               # Entry point
├── Dockerfile                # Container setup
├── requirements.txt
├── schemas.py
└── README.md
```

---

## 🐳 Run with Docker

### 1. Build the image

```bash
docker build -t openenv-app .
```

### 2. Run the container

```bash
docker run openenv-app
```

---

## 🧪 Sample Output

```id="c76n3g"
[START] task=adaptive_learning env=openenv model=baseline
[STEP] step=0 action=show_video reward=2.50 done=false
[STEP] step=1 action=interactive_exercise reward=4.00 done=false
[STEP] step=2 action=revision_notes reward=2.00 done=false
[STEP] step=3 action=give_quiz reward=12.00 done=false
[STEP] step=4 action=take_break reward=0.20 done=false
[END] success=true steps=20
```

---

## 🧠 How It Works

### 🔹 Agent

The agent selects actions based on:

* Concept mastery levels
* Fatigue and engagement
* Learning attempts

It also includes:

* Exploration (randomness)
* Anti-repetition mechanisms

---

### 🔹 Environment

The environment:

* Simulates student learning progression
* Updates mastery based on actions
* Assigns rewards based on effectiveness

---

## 📈 Learning Flow Example

```id="c5jvsh"
Video → Exercise → Exercise → Quiz → Break → Exercise → Quiz
```

👉 This demonstrates a **dynamic and personalized learning path**

---

## 🎯 Key Highlights

* Moves beyond static rule-based systems
* Demonstrates adaptive and feedback-driven behavior
* Fully reproducible using Docker
* Designed for evaluation in AI/ML hackathons

---

## ⚠️ Notes

* Multiple runs may produce different outputs due to exploration
* The system is designed to simulate learning behavior, not real student data

---

## 👥 Team Contribution

* Agent design and adaptive logic
* Environment modeling and reward shaping
* Dockerization and system integration

---

## 🏁 Conclusion

This project showcases how intelligent agents can create **personalized learning experiences** by dynamically adapting content based on user state and feedback.

---

⭐ If you found this interesting, feel free to explore and build on it!
