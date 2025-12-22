# TODO: MedPredict Development Status

## ✅ Completed Tasks

### Project Setup & Infrastructure

- [x] Create project directory structure (`codebase/`, `model/`, `graphics/`, `scripts/`)
- [x] Establish Streamlit main application (`main.py`)
- [x] Create requirements.txt with pinned dependencies
- [x] Generate placeholder models for testing (`model/*.sav`)
- [x] Generate placeholder images (`graphics/*.jpg`)
- [x] Implement `MaternalHealthDashboard` helper class (`codebase/dashboard_graphs.py`)
- [x] Run and verify Streamlit app launches successfully

### Feature Implementation

- [x] **About Us Page** – Navigation, project description, feature overview, placeholder images
- [x] **Pregnancy Risk Prediction** – Input form (5 fields), model loading, scaling, prediction display
- [x] **Fetal Health Prediction** – Input form (21 fields), model loading, prediction display
- [x] **Dashboard** – API integration, bubble chart, pie chart, data display expanders
- [x] Menu navigation using streamlit-option-menu

### Model & Data

- [x] Load fetal health training notebook (`fetal-health-classifier-ipynb.ipynb`)
- [x] Load maternal health training notebook (`maternalhealthriskdetection-ipynb.ipynb`)
- [x] Identify model architectures (Gradient Boosting Classifier for both)
- [x] Extract feature orders from notebooks
- [x] Document model input shapes and scaling requirements

---

## 🚧 In Progress

- [ ] Push to GitHub with README and TODO documentation

---

## 📋 To-Do / Known Issues

### High Priority

#### 1. Replace Placeholder Models with Real Trained Models

- **Status:** Blocked (awaiting real `.sav` files)
- **Task:**
  - Obtain or regenerate `finalized_maternal_model.sav` trained on actual Maternal Health Risk dataset
  - Obtain or regenerate `fetal_health_classifier.sav` trained on actual Fetal Health dataset
  - Export and save the fitted maternal `StandardScaler` as `scaler_maternal_model.sav`
- **Impact:** Current app uses toy models; predictions are not meaningful
- **Effort:** Low (once datasets are available)
- **Depends On:** Access to original training datasets or saved model artifacts

#### 2. Replace Placeholder Images with Real Assets

- **Status:** Not started
- **Task:**
  - Provide or source professional images for:
    - `graphics/pregnancy_risk_image.jpg`
    - `graphics/fetal_health_image.jpg`
  - Update image captions and layout in `main.py` if needed
- **Impact:** UI/UX improvement
- **Effort:** Low
- **Dependencies:** None

#### 3. Improve Fetal Health Input Form UX

- **Status:** Not started
- **Task:**
  - Group 21 inputs into logical sections (Vitals, Decelerations, Variability, Histogram)
  - Replace text inputs with Streamlit number inputs or sliders
  - Add input validation (min/max ranges, type checking)
  - Implement "Fill with Sample" preset button to auto-populate typical/example values
  - Display feature descriptions/tooltips to guide users
- **Impact:** Significantly improves usability
- **Effort:** Medium
- **Dependencies:** None

#### 4. Input Validation & Error Handling

- **Status:** Not started
- **Task:**
  - Add min/max constraints for all numeric inputs (based on training data ranges)
  - Validate inputs before passing to model
  - Handle edge cases (missing values, out-of-range, non-numeric)
  - Provide user-friendly error messages
- **Impact:** Prevents invalid predictions
- **Effort:** Low-Medium
- **Dependencies:** None

### Medium Priority

#### 5. Add Fetal Model Scaler

- **Status:** Not started
- **Task:**
  - Check if fetal model requires input scaling (review notebook)
  - If needed, export and save fetal scaler as `model/scaler_fetal_model.sav`
  - Update `main.py` fetal prediction to apply scaling before prediction
- **Impact:** Ensures correct model behavior if scaler is part of training pipeline
- **Effort:** Low
- **Dependencies:** Access to fetal training notebook details

#### 6. Add Input Ranges & Documentation

- **Status:** Not started
- **Task:**
  - Document expected input ranges for each feature (from training data)
  - Display ranges in UI (e.g., "Age (years): 18–50")
  - Add tooltips or help text for medical parameters
- **Impact:** Guides users on realistic input values
- **Effort:** Low
- **Dependencies:** None

#### 7. Persist Prediction History

- **Status:** Not started
- **Task:**
  - Add optional prediction logging to CSV or SQLite database
  - Display past predictions in a "History" tab
  - Allow export of results
- **Impact:** Enables tracking and analysis of predictions over time
- **Effort:** Medium
- **Dependencies:** None

#### 8. Improve Dashboard

- **Status:** Partial (basic implementation done)
- **Task:**
  - Test API endpoint reliability
  - Handle API failures gracefully
  - Cache data to avoid repeated API calls
  - Add filters/regional selection
  - Improve chart aesthetics and interactivity
- **Impact:** Better data visualization and robustness
- **Effort:** Medium
- **Dependencies:** None

### Low Priority

#### 9. Unit Tests

- **Status:** Not started
- **Task:**
  - Write tests for model loading
  - Write tests for scaling and prediction logic
  - Write tests for dashboard API integration
  - Set up CI/CD (GitHub Actions)
- **Impact:** Improves code reliability
- **Effort:** Medium-High
- **Dependencies:** None

#### 10. Docker & Deployment

- **Status:** Not started
- **Task:**
  - Create Dockerfile for containerization
  - Deploy to Streamlit Cloud, Heroku, AWS, or similar
  - Set up environment variable management for production
- **Impact:** Enables easy sharing and scalable deployment
- **Effort:** Medium
- **Dependencies:** None

#### 11. Model Retraining Pipeline

- **Status:** Not started
- **Task:**
  - Automate periodic model retraining on new data
  - Add model versioning and rollback capabilities
  - Monitor model drift and performance
- **Impact:** Keeps models fresh and performant
- **Effort:** High
- **Dependencies:** Data pipeline infrastructure

#### 12. Mobile Responsiveness

- **Status:** Not started
- **Task:**
  - Test and optimize UI for mobile devices
  - Adjust layout and font sizes for small screens
- **Impact:** Enables use on smartphones/tablets
- **Effort:** Low-Medium
- **Dependencies:** None

#### 13. Multi-Language Support

- **Status:** Not started
- **Task:**
  - Add translations for medical terms and UI strings
  - Implement language selection in sidebar
- **Impact:** Broadens accessibility
- **Effort:** Medium
- **Dependencies:** None

---

## 📊 Quick Reference: What's Working vs. What Isn't

| Feature             | Status          | Notes                                                           |
| ------------------- | --------------- | --------------------------------------------------------------- |
| App Launch          | ✅ Working      | Streamlit runs successfully at localhost:8501                   |
| Navigation Menu     | ✅ Working      | Option menu displays all 4 sections                             |
| About Us Page       | ✅ Working      | Shows overview and placeholder images                           |
| Pregnancy Risk Form | ✅ Partially    | Form loads, scaler works, but model is placeholder              |
| Fetal Health Form   | ✅ Partially    | Form loads (21 fields), but model is placeholder; UX needs work |
| Dashboard           | ✅ Partially    | API integration works, charts render; may need error handling   |
| Model Predictions   | ❌ Not Accurate | Using dummy models; real models needed                          |
| Input Validation    | ❌ Missing      | No range checks or error messages                               |
| Documentation       | ✅ Complete     | README.md and TODO.md created                                   |

---

## 🔗 Dependencies & Blockers

1. **Real Trained Models** – Blocked on obtaining actual `.sav` files or original datasets
2. **Professional Images** – Blocked on asset availability
3. **Medical Domain Knowledge** – May need expert review of input ranges and feature interpretations

---

## 📅 Estimated Completion

- **Critical Path (to functional app):** Replace placeholder models → 1 week
- **High Priority (UX improvements):** Input validation + fetal form redesign → 2 weeks
- **Full Release (with tests, deployment, extras):** 4-6 weeks

---

## 🤝 How to Contribute Next Steps

1. **To unblock high-priority tasks:**

   - Provide real trained model `.sav` files and fitted scaler
   - Or provide original training datasets (Maternal Health Risk, Fetal Health Classification)

2. **To improve UX:**

   - Review fetal form and suggest groupings/reorganization
   - Provide professional images for graphics folder
   - Suggest input validation ranges

3. **To test the app:**
   - Run `streamlit run main.py` and test all four sections
   - Report any bugs or unexpected behavior
   - Test with various input values

---

**Last Updated:** December 22, 2025
