import streamlit as st

from conv import convert_img_format
from io import BytesIO
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

st.set_page_config(page_title="Image Converter")

st.title("Image Converter FASTEKO Edition")
st.write("Convert your images in one click!")

uploaded_file = st.file_uploader (
    "Upload an image",
    type=["PNG", "JPEG", "HEIC", "TIFF", "ICO", "BMP", "JFIF"]
)



if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded image", use_container_width=True)

    st.write(f"Original format: {img.format}")

    format_options = ["PNG", "JPEG", "HEIC", "TIFF", "ICO", "BMP", "JFIF"]
    output_format = st.selectbox(
        "Choose output format", format_options 
    )

    if img.format != output_format:
      if st.button("Convert"):
        converted_img = convert_img_format(img, output_format.lower())

        buf = BytesIO()
        converted_img.save(buf, format=output_format)
        buf.seek(0)

        st.write(f"Image converted to {output_format}")

        st.download_button(
            label=f"Download as {output_format}",
            data=buf,
            file_name=f"image.{output_format.lower()}",
            mime=f"image/{output_format.lower()}"
        )
else:
    st.write("Select a different format!")
     
    
