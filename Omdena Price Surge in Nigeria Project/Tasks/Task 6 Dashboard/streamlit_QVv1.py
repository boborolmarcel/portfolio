import streamlit as st
import os
from nbconvert import HTMLExporter
import nbformat

# ---- Function to display notebooks ----
def display_notebook(notebook_path):
    with open(notebook_path, 'r') as f:
        nb = nbformat.read(f, as_version=4)
    html_exporter = HTMLExporter()
    body, resources = html_exporter.from_notebook_node(nb)
    st.components.v1.html(body, height=1000, scrolling=True)


# ---- Main app ----
st.set_page_config(layout="wide")  # Adjust layout for wide displays

st.sidebar.title("Navigation")
choice = st.sidebar.selectbox("Choose:", ["Notebooks", "Images"])

if choice == "Notebooks":
    # Get the list of notebooks in the 'notebooks' directory
    notebooks = [file for file in os.listdir("notebooks") if file.endswith(".ipynb")]
    selected_notebook = st.sidebar.selectbox("Select Notebook:", notebooks)
    
    if selected_notebook:
        # Create a path to the selected notebook
        notebook_path = os.path.join("notebooks", selected_notebook)
        # Display the selected notebook using the defined function
        display_notebook(notebook_path)
        

elif choice == "Images":
    # Get the list of images in the 'images' directory
    image_files = [file for file in os.listdir("images") if file.endswith((".png", ".jpg", ".jpeg"))]
    # Divide image files into two columns for display
    col1, col2 = st.columns(2)
    
    # Display images in a grid layout (two columns)
    for i, image_file in enumerate(image_files):
        image_path = os.path.join("images", image_file)
        # Alternate image display between columns
        if i % 2 == 0:
            with col1:
                st.image(image_path, caption=image_file)
        else:
            with col2:
                st.image(image_path, caption=image_file)

