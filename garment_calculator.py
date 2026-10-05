# bringing streamlit into our appliction to use it
import streamlit as st
def calculate_production_time(quantity, minutes_per_garment,workers,efficiency):
    total_work_minutes = quantity * minutes_per_garment
    theoretical_minutes = total_work_minutes / workers
    actual_minutes = theoretical_minutes / (efficiency / 100)
    hours = actual_minutes / 60
    return hours

st.title("=== Garment production time predictor ===")
quantity = st.number_input("Quantity", min_value= 0)
minutes_per_garment = st.number_input("Minutes per garment",min_value=0.1)
workers = st.number_input("Workers: ", min_value=1)
efficiency = st.number_input("Efficiency", min_value=0.1)

if st.button("Calculate Production Time"):
    calculated_hours = calculate_production_time(quantity, minutes_per_garment,workers,efficiency)
    st.write("Estimated production time:", round(calculated_hours,2))
