import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib
import seaborn as sns 
import matplotlib.pyplot as plt 

#load the best model 
with open("../model/best_model3.pkl", "rb") as model_file: 
    model= joblib.load(model_file)  

#Function to predict insurance charges 
def predict_charges(age, sex, bmi, smoker, region, children): 
    #Encode the categorical varivable 
    sex_encoded = 1 if sex == "Male" else 0 
    smoker_encoded = 1 if smoker == "Yes" else 0 
    region_mapping ={"northeast":0,"northwest":1,"southeast":2,"southwest":3} 
    region_encoded = region_mapping.get(region.lower(),0) 

    #create input array 
    input_data = np.array([age, sex_encoded, bmi, children,smoker_encoded,region_encoded])  

    # Reshape the data to a 2D array
    input_data = np.array(input_data).reshape(1, -1)

    #predict charges 
    predict_charges = model.predict(input_data)[0] 
    return round(predict_charges,2) 

#streamlit UI 
st.title("Health Insurance Claim Predictor 💰") 
st.write("Predict medical insurance cost based on health & lifesytle factors.")


#sidebar
st.sidebar.header("Enter The Details") 
age = st.sidebar.slider("Age",18,100,30)
sex = st.sidebar.selectbox("Sex",["Male","Female"]) 
bmi = st.sidebar.slider("BMI",10.0,50.0,25.0)
smoker = st.sidebar.radio("Smoker?",["yes","No"])
region =st.sidebar.selectbox("Region",["northeast", "northwest", "southeast", "southwest"])
children = st.sidebar.slider("No. of Children",0,5,1) 


#predict button
if st.sidebar.button("Predict Claim"): 
    predicted_cost = predict_charges(age, sex, bmi, smoker, region,  children) 
    # Display the predicted cost
    st.success(f"Predicted Insurance Cost: ₹{predicted_cost} INR")
#data visualization 
st.subheader("Impact of BMI & Smoking on Claim") 
sample_data = pd.DataFrame({
    "bmi":np.random.uniform(10,50,100),
    "claim":np.random.uniform(1000, 50000, 100),
    "smoker":np.random.choice(["Yes", "No"], 100)
}
)

fig, ax = plt.subplots() 
sns.scatterplot(data=sample_data, x= "bmi",y="claim", hue="smoker",ax =ax)
st.pyplot(fig) 

#Show correlation heatmap 

st.subheader("Feature Correlation Heatmap") 
# Create a new DataFrame with only numeric columns for correlation
numeric_data = sample_data.select_dtypes(include=[np.number])
corr_matrix = numeric_data.corr() 
fig, ax = plt.subplots() 
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm",ax=ax) 
st.pyplot(fig) 

#footer 
st.write("Developed by Joseph")