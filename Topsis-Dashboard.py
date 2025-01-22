import streamlit as st
import pandas as pd
import numpy as np

def topsis(data, weights, impacts):
    # Normalize the decision matrix
    norm_data = data / np.sqrt((data**2).sum())
    # Weighted normalized decision matrix
    weighted_data = norm_data * weights
    # Ideal (best) and negative ideal (worst) solutions
    ideal_best = np.where(impacts == '+', weighted_data.max(axis=0), weighted_data.min(axis=0))
    ideal_worst = np.where(impacts == '+', weighted_data.min(axis=0), weighted_data.max(axis=0))
    # Calculate distances from ideal solutions
    dist_best = np.sqrt(((weighted_data - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst)**2).sum(axis=1))
    # Calculate the TOPSIS score
    scores = dist_worst / (dist_best + dist_worst)
    return scores

# Streamlit UI
st.title("TOPSIS Decision-Making Dashboard")

# File upload
uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Uploaded Dataset:")
    st.write(data)

    # Input parameters for TOPSIS
    criteria_columns = st.multiselect("Select criteria for analysis:", options=data.columns)
    weights = st.text_input("Enter weights for the criteria (comma-separated):", value="1,1,1")
    impacts = st.text_input("Enter impacts for the criteria (comma-separated, use '+' for beneficial and '-' for non-beneficial):", value="+,+,+")

    # Convert inputs to arrays
    try:
        weights = np.array([float(w) for w in weights.split(",")])
        impacts = np.array([i.strip() for i in impacts.split(",")])

        if len(criteria_columns) == len(weights) == len(impacts):
            if st.button("Run TOPSIS"):
                # Subset data and run TOPSIS
                subset_data = data[criteria_columns].astype(float)
                scores = topsis(subset_data, weights, impacts)
                data["TOPSIS Score"] = scores
                data = data.sort_values(by="TOPSIS Score", ascending=False)
                data["Rank"] = range(1, len(data) + 1)

                # Display results
                st.write("Results:")
                st.write(data)

                # Download results
                csv = data.to_csv(index=False)
                st.download_button("Download Results", data=csv, file_name="topsis_results.csv", mime="text/csv")
        else:
            st.error("Ensure weights, impacts, and criteria columns are of the same length.")
    except ValueError:
        st.error("Please enter valid weights and impacts.")
