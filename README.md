## **TOPSIS Decision-Making Dashboard**
APP LINK --> https://topsisayushpanwar.streamlit.app/
---

### **Overview**
The **TOPSIS Decision-Making Dashboard** is an interactive tool that helps users rank alternatives based on multiple criteria using the **TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)** method. Users can upload their datasets, specify weights and impacts for each criterion, and receive rankings based on TOPSIS scores.

---

### **Features**
1. Upload any decision matrix dataset in CSV format.
2. Select criteria for evaluation.
3. Specify weights for the criteria.
4. Define the impact of each criterion (beneficial or non-beneficial).
5. Automatically normalize and calculate TOPSIS scores.
6. View ranked results and download the output as a CSV file.

---

### **Installation**

#### Prerequisites:
- Python 3.7 or higher
- Required libraries: `streamlit`, `pandas`, `numpy`

#### Steps:
1. Clone or download this repository.
2. Install the required libraries using:
   ```bash
   pip install streamlit pandas numpy
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
   Replace `app.py` with the filename of the script.

---

### **How to Use**
1. **Upload Dataset**:
   - Upload a CSV file containing your decision matrix.
   - Ensure the dataset has column headers and numeric values for the criteria.

2. **Select Criteria**:
   - Choose the columns (criteria) you want to analyze from the dataset.

3. **Specify Weights**:
   - Enter the weights for each criterion as a comma-separated list (e.g., `1,2,1`).
   - Ensure the weights correspond to the selected criteria.

4. **Specify Impacts**:
   - Define the impact for each criterion as a comma-separated list:
     - Use `+` for beneficial criteria (higher is better).
     - Use `-` for non-beneficial criteria (lower is better).

5. **Run TOPSIS**:
   - Click on the "Run TOPSIS" button to calculate scores and rankings.
   - The results will be displayed in a table.

6. **Download Results**:
   - Download the ranked dataset as a CSV file by clicking the "Download Results" button.

---

### **Input Format**
The input dataset should be a CSV file with the following:
- **Columns**: Each column represents a criterion.
- **Rows**: Each row represents an alternative (option to evaluate).
- **Numeric values**: All criteria must have numeric values.

Example:
| Alternative | Criterion 1 | Criterion 2 | Criterion 3 |
|-------------|-------------|-------------|-------------|
| A1          | 100         | 50          | 30          |
| A2          | 90          | 40          | 20          |
| A3          | 80          | 70          | 60          |

---

### **Outputs**
The output includes:
1. The original dataset with two new columns:
   - **TOPSIS Score**: The calculated score for each alternative.
   - **Rank**: The ranking based on the TOPSIS score.
2. Downloadable CSV file with the results.

---

### **Error Handling**
- If weights, impacts, or criteria columns are not of the same length, an error message will be displayed.
- Non-numeric values in the selected criteria columns will result in an error.
- Ensure proper formatting of weights and impacts to avoid invalid input errors.

---

### **Customization**
- Modify the normalization method in the `topsis` function as needed.
- Adjust the Streamlit UI elements (e.g., themes, layouts) for better user experience.

---
Enjoy using the TOPSIS Decision-Making Dashboard! 🚀
