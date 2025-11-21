Medical Insurance Cost Prediction App
🚀 An end-to-end Machine Learning project to predict medical insurance costs using Python, Streamlit, Docker, and CI/CD pipelines.


Project Overview
This project demonstrates a complete ML deployment pipeline, delivering real-time insurance cost predictions through a seamless, interactive user experience.

- Trains a regression model using historical insurance data.
- Builds a web-based app in Streamlit for easy user input and live predictions.
- Containerizes the solution using Docker for reliable, repeatable deployments across platforms.
- Automates build, test, and deploy steps using GitHub Actions to ensure fast release cycles and reduced manual overhead.

Features
Interactive Streamlit App
Enter age, BMI, children, smoking habits, and region to receive cost predictions instantly.

Dockerized Application
- Ensures reproducibility, easy local launch, and cloud compatibility.

CI/CD Pipeline
- GitHub Actions runs unit tests, builds images, and deploys automatically with every repository update.

End-to-End ML Workflow
- Everything from data preprocessing and model training to web serving and deployment is covered.

Architecture & Workflow

medical-insurance-cost-prediction-ci-cd/
├── Dockerfile
├── streamlit_app.py
├── model.pkl
├── requirements.txt
└── .github/
    └── workflows/
        └── ci-cd.yml
Workflow:
Code → Push to GitHub → GitHub Actions CI/CD → Docker Build → Streamlit App Running in Container

Quick Start
bash
# Clone the Repository
git clone https://github.com/vinayak533/medical-insurance-cost-prediction-ci-cd.git

# Build the Docker image
docker build -t med-insurance-app .

# Run the container
docker run -p 8501:8501 med-insurance-app

# Access the app in your browser
# Open http://localhost:8501
Implementation Details
Data: Uses insurance datasets with labeled costs.

Model: Trained regression (e.g., Linear Regression) stored as model.pkl.

App: Streamlit interface for easy input/output.

CI/CD: YAML workflows in .github/workflows/ automate build, test, and deployment.

Future Improvements
- Cloud deployment (Heroku/AWS/GCP).

- User authentication.

- Model explainability & analytics dashboard.

- Enhanced unit and integration testing.

Contact :
Maintained by Vinayak K V – open to feedback and collaboration!


