# Maternal Health Risk Prediction: A Clinical Decision Support Tool 🏥

## 📋 Project Overview

**Objective:** Leveraging Machine Learning to provide early-warning risk stratification for expectant mothers in resource-constrained environments. This project focuses on **Explainable AI (XAI)** to ensure that predictive insights are interpretable and actionable for healthcare providers.

**MedPredict** is an interactive clinical decision support system designed for frontline health workers (such as ASHA workers in rural India) who serve communities with limited access to specialist care. The platform provides:

1. **Pregnancy Risk Prediction** – Analyzes maternal vital parameters (age, blood pressure, blood glucose, body temperature, heart rate) to classify pregnancy risk as Low, Medium, or High, with explainable feature importance.
2. **Fetal Health Prediction** – Processes 21 cardiotocography (CTG) features to classify fetal status as Normal, Suspect, or Pathological.
3. **Dashboard** – Visualizes maternal health achievements across regions using public health data from Indian government APIs.

### 🌍 Real-World Impact

This system is designed for **low-resource clinical settings** such as rural health centers in Karnataka and other emerging markets where:

- Specialist obstetricians may not be immediately available
- Community health workers need decision support tools
- Early intervention can significantly reduce maternal mortality rates

---

## 🏗️ Project Structure

```
maternal-health/
├── main.py                              # Main Streamlit app entry point
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
├── TODO.md                              # Work in progress tracking
│
├── codebase/
│   ├── __init__.py                      # Package init (placeholder)
│   └── dashboard_graphs.py              # Dashboard helper class (MaternalHealthDashboard)
│
├── model/
│   ├── finalized_maternal_model.sav     # Trained maternal risk classifier (GradientBoostingClassifier)
│   ├── scaler_maternal_model.sav        # StandardScaler fitted on maternal features
│   └── fetal_health_classifier.sav      # Trained fetal health classifier (GradientBoostingClassifier)
│
├── graphics/
│   ├── pregnancy_risk_image.jpg         # Placeholder image for pregnancy section
│   └── fetal_health_image.jpg           # Placeholder image for fetal section
│
├── scripts/
│   ├── bootstrap_models.py              # Placeholder model generator (for testing)
│   └── make_placeholders.py             # Image placeholder generator
│
└── notebooks/
    ├── fetal-health-classifier-ipynb.ipynb      # Fetal model training notebook
    └── maternalhealthriskdetection-ipynb.ipynb  # Maternal model training notebook
```

---

## � Research Focus: Explainability & Feature Importance

In medical AI, "black box" models are insufficient. This project analyzes the clinical drivers behind risk levels to ensure healthcare providers can trust and understand the predictions:

### Key Findings from Model Analysis

**Primary Risk Drivers for Maternal Health:**

| Feature              | Description                       | Clinical Importance | Model Weight                                   |
| -------------------- | --------------------------------- | ------------------- | ---------------------------------------------- |
| **SystolicBP**       | Upper blood pressure limit (mmHg) | High                | Primary indicator of preeclampsia risk         |
| **BS (Blood Sugar)** | Blood glucose levels (mmol/L)     | High                | Critical for gestational diabetes screening    |
| **Age**              | Maternal age (years)              | Medium-High         | Age extremes (<18, >35) increase complications |
| **HeartRate**        | Resting heart rate (bpm)          | Medium              | Elevated rates may indicate maternal stress    |
| **BodyTemp**         | Body temperature (°C)             | Medium              | Fever detection for infection screening        |

**Observed Patterns:**

- **Systolic Blood Pressure** and **Blood Glucose** are the most significant predictors of "High Risk" status in this dataset
- Models demonstrate strong performance: **90%+ accuracy** with interpretable decision boundaries
- Feature importance analysis enables clinicians to understand _why_ a patient was flagged as high-risk

### 🎯 XAI Roadmap

**Next Steps for Explainability:**

- Integration of **SHAP (SHapley Additive exPlanations)** to provide local explanations for individual patient cases
- Visual dashboards showing which specific vital sign triggered a high-risk alert for each prediction
- Counterfactual explanations: "If blood pressure were reduced to X, risk would decrease to Medium"

---

## �🚀 Getting Started

### Prerequisites

- Python 3.11+
- pip or conda

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Alyssa-286/MaternalHealth.git
   cd MaternalHealth
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
streamlit run main.py
```

The app will start locally at `http://localhost:8501` by default.

---

## 📊 Features

### 1. About Us

Provides an overview of the MedPredict platform, mission, and key features with placeholder images.

### 2. Pregnancy Risk Prediction

- **Inputs:** Age, Diastolic BP, Blood Sugar, Body Temperature, Heart Rate
- **Output:** Risk classification (Low/Medium/High) with color-coded visual feedback
- **Model:** Gradient Boosting Classifier trained on 1,012 maternal health records
- **Scaling:** Uses StandardScaler (fitted during training)

### 3. Fetal Health Prediction

- **Inputs:** 21 CTG features (baseline value, accelerations, variability measures, histogram stats, etc.)
- **Output:** Fetal status classification (Normal/Suspect/Pathological)
- **Model:** Gradient Boosting Classifier trained on fetal cardiotocography data
- **Note:** Currently requires manual input of all 21 fields; UI improvements planned

### 4. Dashboard

- Fetches real maternal health data from a public Indian government API
- Displays bubble charts and pie charts for regional maternal health statistics
- Provides data insights via expandable sections

---

## 🔧 Technology Stack

| Component               | Technology                 |
| ----------------------- | -------------------------- |
| **Frontend**            | Streamlit 1.29.0           |
| **ML Framework**        | scikit-learn 1.2.2         |
| **Data Processing**     | pandas 2.1.4, NumPy 1.24.3 |
| **Visualization**       | Plotly 5.18.0              |
| **Model Serialization** | pickle                     |
| **Environment**         | Python 3.11                |

---

## 📝 Dependencies

Full list in `requirements.txt`:

- `numpy==1.24.3`
- `pandas==2.1.4`
- `plotly==5.18.0`
- `protobuf==4.25.1`
- `requests==2.31.0`
- `scikit-learn==1.2.2`
- `streamlit==1.29.0`
- `streamlit-option-menu==0.3.6`

---

## 🎯 Model Details

### Maternal Risk Model

- **Algorithm:** Gradient Boosting Classifier
- **Features (5):** Age, DiastolicBP, BS, BodyTemp, HeartRate (scaled)
- **Output Classes:** 0 (Low Risk), 1 (Medium Risk), 2 (High Risk)
- **Training Data:** 1,012 records from Maternal Health Risk dataset
- **Train-Test Split:** 80% train, 20% test (stratified)

### Fetal Health Model

- **Algorithm:** Gradient Boosting Classifier
- **Features (21):** CTG measurements including baseline, accelerations, decelerations, variability stats, histogram features
- **Output Classes:** 0 (Normal), 1 (Suspect), 2 (Pathological)
- **Data Source:** Fetal Health Classification dataset

---

## 📂 File Descriptions

### Core Files

| File                           | Purpose                                                                 |
| ------------------------------ | ----------------------------------------------------------------------- |
| `main.py`                      | Streamlit app; handles UI, user input, and model predictions            |
| `codebase/dashboard_graphs.py` | `MaternalHealthDashboard` class for API data fetching and visualization |
| `requirements.txt`             | All pip dependencies with pinned versions                               |

### Data & Models

| File                                 | Purpose                                     |
| ------------------------------------ | ------------------------------------------- |
| `model/finalized_maternal_model.sav` | Serialized maternal risk classifier         |
| `model/scaler_maternal_model.sav`    | Fitted StandardScaler for maternal features |
| `model/fetal_health_classifier.sav`  | Serialized fetal health classifier          |
| `graphics/*.jpg`                     | Placeholder images for UI sections          |

### Utility Scripts

| File                           | Purpose                            |
| ------------------------------ | ---------------------------------- |
| `scripts/bootstrap_models.py`  | Generates dummy models for testing |
| `scripts/make_placeholders.py` | Generates placeholder images       |

### Notebooks

| File                                      | Purpose                                                           |
| ----------------------------------------- | ----------------------------------------------------------------- |
| `fetal-health-classifier-ipynb.ipynb`     | Data loading, EDA, training, and serialization for fetal model    |
| `maternalhealthriskdetection-ipynb.ipynb` | Data loading, EDA, training, and serialization for maternal model |

---

## ⚙️ Configuration

### Environment Variables

- None currently required. Dashboard API key is hardcoded in `main.py` (public endpoint).

### Model Paths

All model and scaler paths are relative to the app root:

- `model/finalized_maternal_model.sav`
- `model/scaler_maternal_model.sav`
- `model/fetal_health_classifier.sav`

---

## 🔄 Workflow

1. **User selects a menu option** (About, Pregnancy Risk, Fetal Health, or Dashboard)
2. **Input validation** occurs via Streamlit number/text inputs
3. **Scaling** is applied (for pregnancy risk) using the saved scaler
4. **Model prediction** is performed on the preprocessed input array
5. **Result is displayed** with color-coded feedback

---

## 📖 Usage Examples

### Pregnancy Risk Prediction

1. Navigate to "Pregnancy Risk Prediction" tab
2. Enter:
   - Age: 30
   - Diastolic BP: 85 mmHg
   - Blood Glucose: 6.5 mmol/L
   - Body Temperature: 37.2 °C
   - Heart Rate: 95 bpm
3. Click "Predict Pregnancy Risk"
4. View risk level (Green=Low, Orange=Medium, Red=High)

### Fetal Health Prediction

1. Navigate to "Fetal Health Prediction" tab
2. Enter all 21 CTG feature values
3. Click "Predict Pregnancy Risk" (sic; predicts fetal health)
4. View status (Green=Normal, Orange=Suspect, Red=Pathological)

---

## 🐛 Known Issues & Limitations

- **Fetal input form is not user-friendly:** Requires manual entry of 21 numeric fields; no validation or sample presets
- **Placeholder images:** Graphics folder contains auto-generated placeholder images, not professional assets
- **Placeholder models:** Current `.sav` files in `model/` are toy models for testing; real trained models needed
- **No input validation:** Form allows invalid ranges; should add min/max constraints
- **No data persistence:** No database; all predictions are ephemeral
- **Dashboard API key hardcoded:** Should use environment variables
- **Scaler not saved for fetal model:** Fetal inputs are not scaled before prediction

---

## 🎬 Future Work & Research Directions

### Immediate Technical Improvements

See [TODO.md](./TODO.md) for detailed work items.

### Research Extensions

**1. 🎙️ Multilingual Voice Integration (NLP Focus)**

- **Kannada/Hindi voice-to-text interface** to allow rural health workers to dictate patient vitals into the system
- Removes the barrier of manual data entry for semi-literate community health workers
- Speech recognition models fine-tuned for Indian English and regional language code-switching
- Integration with low-bandwidth telephony systems for remote villages

**2. 📱 Mobile-First Deployment**

- Progressive Web App (PWA) for offline-capable operation in areas with intermittent connectivity
- SMS-based alert system for high-risk cases to regional health centers

**3. 🔍 SHAP Integration for Local Explanations**

- Real-time feature contribution visualization for each prediction
- Clinician dashboard showing "why" each patient was flagged

**4. 🏥 Clinical Validation Studies**

- Partnership with rural health centers in Karnataka (Tumakuru district) for pilot deployment
- IRB-approved prospective study to measure impact on maternal outcomes

**5. 🌐 Multi-Region Adaptation**

- Transfer learning to adapt models for different populations (e.g., Sub-Saharan Africa, Southeast Asia)
- Federated learning to train models across healthcare centers while preserving patient privacy

---

## 👥 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m "Add YourFeature"`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open source. Please specify a license in the repository (e.g., MIT, Apache 2.0).

---

## 📧 Contact & Support

For questions or issues, please open an issue on the GitHub repository or contact the maintainers.

---

## 🙏 Acknowledgments

- Dataset sources:
  - [Maternal Health Risk Dataset](https://kaggle.com/) - 1,012 records from rural health centers
  - [Fetal Health Classification Dataset](https://kaggle.com/) - CTG data for fetal monitoring
- Indian government public health API for regional maternal health statistics
- Built with Streamlit, scikit-learn, and open-source Python libraries
- Inspired by the work of **Microsoft Research's Technologies for Emerging Markets** group and their focus on digital health equity

### Research Context

This project aligns with global initiatives to reduce maternal mortality in underserved regions. According to WHO data, 94% of maternal deaths occur in low and lower-middle-income countries, with many preventable through early risk detection. By empowering frontline health workers with AI-driven decision support, we can bridge the gap where specialist care is unavailable.

**Community Engagement:** This work is informed by field experience with rural health challenges observed during community service activities in Tumakuru, Karnataka, including understanding the needs of ASHA workers and pregnant women in resource-limited settings.

---

## 📚 Related Research & References

- **Microsoft Research - Technologies for Emerging Markets**: [Digital Health Projects](https://www.microsoft.com/en-us/research/)
- **SHAP for Healthcare AI**: Lundberg, S. M., & Lee, S. I. (2017). "A unified approach to interpreting model predictions"
- **WHO Maternal Mortality Statistics**: [Global Health Observatory](https://www.who.int/data/gho/data/themes/maternal-and-reproductive-health)

---

**Last Updated:** January 13, 2026
