import streamlit as st
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder


# Please start the FastAPI server and local LLM server before running this Streamlit app
# Define the FastAPI endpoint
FASTAPI_ENDPOINT = "http://127.0.0.1:7890/calibrate_report/"

# Example pairs of CT and CXR reports
example_reports = {
    "Example 1": {
        "CXR": "No significant findings on the chest X-ray.",
        "CT": "Moderate pleural effusion on the left side, with bilateral opacities."
    },
    "Example 2": {
        "CXR": "Mild opacity suggestive of infectious process.",
        "CT": "Right lower lobe consolidation with associated air bronchograms."
    },
    "Example 3": {
        "CXR": "Normal cardiac silhouette, clear lung fields.",
        "CT": "No acute pulmonary embolism; normal vascular structures."
    },
    "Example 4": {
        "CXR": "PA and lateral chest radiographs demonstrate normal cardiomediastinal silhouette.  Lung fields are clear and without evidence of focal consolidation, nodules, or masses.  No pleural effusions or pneumothorax are identified.  Diaphragms are normally positioned",
        "CT": "Chest CT scan performed without contrast demonstrates no acute cardiopulmonary abnormality.  Lung parenchyma is unremarkable.  No evidence of nodules, masses, lymphadenopathy, or pleural disease.  Mediastinal structures are normal in size and position."
    },
    "Example 5": {
        "CXR": "PA and lateral chest radiographs reveal an area of airspace opacity in the right lower lobe, consistent with pneumonia.  Consideration should be given to further imaging and clinical correlation.",
        "CT": "Chest CT scan demonstrates a right lower lobe consolidation with air bronchograms, findings consistent with pneumonia.  There is no evidence of abscess formation or pleural effusion.  Some surrounding ground-glass opacities are also noted."
    },
    "Example 6": {
        "CXR": "PA and lateral chest radiographs show a suspicious right upper lobe mass.  Further imaging is recommended for characterization.",
        "CT": "Chest CT scan reveals a 3cm spiculated mass in the right upper lobe, concerning for malignancy.  There is evidence of hilar and mediastinal lymphadenopathy.  Biopsy is recommended for tissue diagnosis."
    }
}

st.set_page_config(page_title="CXR Report Calibration", page_icon="📑")

# Create the Streamlit interface
st.title("Chest X-Ray Report Calibration")
st.markdown("Calibrate your CXR report based on the CT report below.")
st.markdown("Please enter the original CXR and CT reports in the text areas below or use our example reports.")

# Add a placeholder option for the example selection
selected_example = st.selectbox("Choose an example report (optional):", [""] + list(example_reports.keys()))

# Pre-fill input areas with the selected example
if selected_example:
    CXR_report_original = example_reports[selected_example]["CXR"]
    CT_report_original = example_reports[selected_example]["CT"]
else:
    CXR_report_original = ""
    CT_report_original = ""

# Display pre-filled reports
CXR_report_original = st.text_area("CXR Report:", value=CXR_report_original, height=150, placeholder="Enter your chest X-ray report here (or choose an example)")
CT_report_original = st.text_area("CT Report:", value=CT_report_original, height=150, placeholder="Enter your chest CT report here (or choose an example)")


# Submit button
if st.button("Submit"):
    # Ensure both inputs are filled
    if CXR_report_original and CT_report_original:
        # Create a MultipartEncoder object
        m = MultipartEncoder(
            fields={
                'cxr_report': CXR_report_original,
                'ct_report': CT_report_original
            }
        )
        # Make a request to the FastAPI server
        response = requests.post(
            FASTAPI_ENDPOINT,
            data=m,
            headers={'Content-Type': m.content_type}
        )
        # Check the response
        if response.status_code == 200:
            calibrated_report = response.text
            st.subheader("Calibrated CXR Report:")
            st.text(calibrated_report)
        else:
            st.error(f"Error: Could not calibrate the report. Status code: {response.status_code}")
            st.error(f"Error message: {response.text}")
    else:
        st.warning("Please fill in both CXR and CT reports before submitting.")