import rembg
import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import io

# Settings
page_title = "Image Background Remover"
page_icon = ":maple_leaf:"
layout = "centered"

# Page Config
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + ":100:" )


# Hide Streamlit Style
hide_st_style = """
        <style>
        #MainMenu {visibility: hidden;}
        .stActionButton div{visibility: hidden;}
        #header {visibility: hidden;}
        #footer {visibility: hidden;}
        </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


# Function to remove background
def remove_background(image, bg_color):
    try:
        np_img = np.array(image)
        result = rembg.remove(np_img)
        if bg_color:
            result = Image.fromarray(result).convert("RGBA")
            background = Image.new("RGBA", result.size, bg_color)
            final_img = Image.alpha_composite(background, result)
            return final_img.convert("RGB")
        return Image.fromarray(result)
    except Exception as e:
        st.error(f"Error removing background: {e}")
        return image


# Title and Info Section
st.markdown("### Welcome to the Image Background Remover app!")
st.info("""
This tool allows you to easily remove the background from your images in one click. 
By default, the background is set to white, but you can choose any color you like.
""")


st.markdown("*Demonstration for Removing Image background*")
with st.expander("Background Remover Example:", expanded=False):
    with st.container():
        # Create two columns for comparison view
        col4, col5 = st.columns(2)

        with col4:
            st.image("media/ronaldo.jpg", caption='Before Edit', use_column_width=True)
        with col5:
            st.image("media/ronaldo_after.png", caption='After Edit', use_column_width=True)

    with st.container():
        # Create two columns for comparison view
        col6, col7 = st.columns(2)

        with col6:
            st.image("media/car.jpg", caption='Before Edit', use_column_width=True)

        with col7:
            st.image("media/car_after.png", caption='After Edit', use_column_width=True)
st.markdown("---")


# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display the images side by side in a container with a border
    with st.container():
        st.write("### Image Comparison")

        # Create two columns for comparison view
        col1, col2 = st.columns(2)

        # Original image preview
        with col1:
            st.image(uploaded_file, caption='Original Image', use_column_width=True)

        # Select background color
        bgcolor = st.color_picker("Pick a background color", "#ffffff")

        # Remove background and show processed image
        with col2:
            output_image = remove_background(Image.open(uploaded_file), bgcolor)
            st.image(output_image, caption='Processed Image', use_column_width=True)

    # Provide download link
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button("Download Image", data=byte_im, file_name="processed_image.png", mime="image/png")

else:
    st.warning("Please upload an image to proceed.")
