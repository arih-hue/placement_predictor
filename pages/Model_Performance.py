import streamlit as st
st.title("Model Performance")
st.write("Performance of the Machine Learning models.")
st.divider()
st.header("Placement Prediction")
col1, col2 = st.columns(2)
with col1:
    st.metric(
        "Train Accuracy",
        "87.23%"
    )
with col2:
    st.metric(
        "Test Accuracy",
        "86.09%"
    )
st.write("")
st.subheader("Confusion Matrix")
st.image(
    "assets/confusion_matrix.png",
    use_container_width=True
)
st.write("")
st.subheader("Feature Importance")
st.image(
    "assets/classifier_importance.png",
    use_container_width=True
)
st.divider()
st.header("Salary Prediction")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "R² Score",
        "0.93"
    )
with col2:
    st.metric(
        "MAE",
        "0.78"
    )
with col3:
    st.metric(
        "RMSE",
        "1.95"
    )
st.write("")
st.subheader("Feature Importance")
st.image(
    "assets/regressor_importance.png",
    use_container_width=True
)
st.write("")
st.subheader("Actual vs Predicted")
st.image(
    "assets/actual_vs_predicted.png",
    use_container_width=True
)
st.write("")
st.subheader("Residual Plot")
st.image(
    "assets/residual_plot.png",
    use_container_width=True
)