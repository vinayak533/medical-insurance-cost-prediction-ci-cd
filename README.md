# Medical Insurance Cost Prediction App

🚀 **An end-to-end Machine Learning project to predict medical insurance costs using Python, Streamlit, Docker, and CI/CD pipelines.**

---

## **Project Overview**

This project demonstrates a full ML deployment workflow:

- Train a model to predict medical insurance costs.
- Build a **Streamlit app** for interactive predictions.
- Containerize the app using **Docker** for consistent deployment.
- Automate build, test, and deployment using **GitHub Actions CI/CD**.

---

## **Features**

- **Interactive Streamlit App**  
  Users can input details like age, BMI, number of children, smoking habits, and more to get insurance cost predictions.

- **Dockerized Application**  
  - Containerized for reproducibility and easy deployment.  
  - Run locally or deploy to cloud platforms seamlessly.

- **CI/CD Pipeline**  
  - Automated build, test, and deployment using GitHub Actions.  
  - Ensures app is always updated with the latest code.  

- **End-to-End ML Workflow**  
  - Code → GitHub Actions → Docker build → Streamlit app running in container.

---

## **Architecture / Workflow**

medical-insurance-cost-prediction-ci-cd/
├── Dockerfile
├── streamlit_app.py
├── model.pkl
├── requirements.txt
└── .github/
    └── workflows/
        └── ci-cd.yml

