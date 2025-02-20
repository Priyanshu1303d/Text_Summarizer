# 📌  End to End Text_Summarizer Project 


## workflow:
 1. Update the config.yaml
 2. Update the params.yaml
 3. Update entity
 4. Update Configuration Manager in src config
 5. Update the components
 6. Update the pipeline
 7. Update the main.py
 8. Update the app.py


This project follows a modular, pipeline-based approach to **Text Summarization** using deep learning. Below is the structured workflow followed for this project:

## 🛠️ Workflow Steps:

### 1️⃣ Update `config.yaml`
- The `config.yaml` file contains all the **configurations** required for the project, such as dataset paths, model parameters, and training configurations.
- This ensures a **centralized** place to modify parameters without altering the main code.

### 2️⃣ Update `params.yaml`
- Stores **hyperparameters** like learning rate, batch size, and model-specific settings.
- Helps in maintaining **experiments reproducibility** and fine-tuning model performance.

### 3️⃣ Update `entity`
- Defines **dataclasses** (e.g., `DataIngestionConfig`, `ModelTrainingConfig`) to ensure structured access to configurations.
- Avoids hardcoding and makes the code **cleaner and type-safe**.

### 4️⃣ Update `Configuration Manager` in `src/config`
- Reads values from `config.yaml` and `params.yaml` and **returns structured objects**.
- Acts as an interface between raw YAML files and Python code, improving **maintainability**.

### 5️⃣ Update `components`
- Implements core functions such as:
  - **Data Ingestion** (downloading and preprocessing data)
  - **Model Training** (building and training the summarization model)
  - **Evaluation** (measuring model performance)
  - **Prediction** (generating text summaries)
- Each function is **modular**, making debugging and updates easier.

### 6️⃣ Update `pipeline`
- Combines all components into a **sequential pipeline**.
- Ensures that each step (data ingestion → preprocessing → training → evaluation) runs in the correct order.

### 7️⃣ Update `main.py`
- The **entry point** of the project that triggers the entire pipeline.
- Calls all necessary modules to run the end-to-end summarization workflow.

### 8️⃣ Update `app.py`
- Develops a **Flask/FastAPI web interface** to deploy and interact with the model.
- Allows users to input text and receive summarized outputs via an API or UI.

---

## 🔥 Why Follow This Workflow?
✅ **Modular & Scalable** – Easy to modify individual components without affecting the whole project.  
✅ **Reproducible** – Configuration files make it simple to rerun experiments with different settings.  
✅ **Deployment Ready** – The structured approach makes model integration into real-world applications seamless.  
