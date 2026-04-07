# openAI_project

build in openAI_project  API key

OpenEnv Hackathon Project

A simple Reinforcement Learning (RL) project built using **Gymnasium**.
This project demonstrates how to create a custom environment and train a basic agent to interact with it.

---

## 📌 Project Overview

This project implements:

* A custom grid-based environment
* A simple random agent
* Training loop for interaction
* Modular and scalable project structure

The agent starts at position `(0,0)` and tries to reach a goal position in a grid.

---

## 🏗️ Project Structure

openenv-hackathon/
├── README.md
├── requirements.txt
├── config/
│   ├── base_config.yaml
│   └── env_config.yaml
├── src/
│   ├── envs/
│   │   ├── custom_env.py
│   │   └── utils.py
│   ├── agents/
│   │   └── simple_agent.py
│   ├── training/
│   │   ├── trainer.py
│   │   └── logger.py
│   └── utils/
│       └── helpers.py
├── tests/
│   ├── test_env.py
│   └── test_agent.py
└── notebooks/
    └── prototype.ipynb

## ⚙️ Installation

### 1. Clone the repository

git clone <https://github.com/dnyaneshwaripachankar-droid/openAI_project>
cd openenv-hackathon

### 2. Install dependencies

pip install -r requirements.txt

## ▶️ How to Run

Run the training script:

python -m src.training.trainer

---

## 🧠 How It Works

### Environment

* Grid world of size `N x N`
* Agent starts at `(0,0)`
* Goal position defined in config
* Actions:

  * 0 → Up
  * 1 → Down
  * 2 → Left
  * 3 → Right

### Rewards

* +1 → when goal is reached
* -0.1 → for each step (penalty to encourage faster learning)

---

## ⚙️ Configuration

### `env_config.yaml`

environment:
  grid_size: 5
  goal_position: [4, 4]

### `base_config.yaml`

training:
  episodes: 10
  max_steps: 50

---

## 🧪 Running Tests

Install pytest:

pip install pytest

Run tests:

pytest

---

## 📓 Notebook Demo

Open the notebook:

notebooks/prototype.ipynb

This notebook allows you to:

* Test environment manually
* Run agent step-by-step
* Visualize rewards

---

## ⚠️ Common Issues & Fixes

### ModuleNotFoundError

No module named 'src'

✔ Fix:

python -m src.training.trainer

---

### Relative Import Errors

✔ Always run from project root directory

---

## 🚀 Future Improvements

* Implement Q-Learning algorithm
* Add Deep Q-Network (DQN)
* Add visualization (grid UI)
* Save trained model
* Add performance metrics

---

## 🎯 Learning Outcomes

* Understand Reinforcement Learning basics
* Learn custom environment design
* Work with Gymnasium
* Practice modular Python project structure

---

## 👨‍💻 Author

Developed as part of OpenEnv Hackathon Project.

---

## ⭐ Contribution

Feel free to fork, improve, and submit pull requests!

---

## works

Environment
Grid world of size N x N
Agent starts at (0,0)
Goal position defined in config
Actions:
0 → Up
1 → Down
2 → Left
3 → Right
Rewards
+1 → when goal is reached
-0.1 → for each step (penalty to encourage faster learning)
