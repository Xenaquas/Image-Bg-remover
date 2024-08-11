# Image Background Remover

## Overview

Welcome to the Image Background Remover app! This simple and user-friendly web application allows you to remove the background from your images effortlessly. By default, the background is set to white, but you can choose any color you like for the background.

## Features

- **Image Upload**: Upload images in PNG, JPG, or JPEG format.
- **Background Removal**: Automatically remove the background from the uploaded image using `rembg`.
- **Custom Background Color**: Choose a custom background color for the processed image.
- **Comparison View**: View the original and processed images side by side for easy comparison.
- **Download Option**: Download the processed image in PNG format.
- **User-Friendly Interface**: Clean and intuitive design with easy-to-use controls.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/image-background-remover.git
    ```
2. Change to the directory:
    ```bash
    cd image-background-remover
    ```
3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Requirements

- Python 3.7+
- Streamlit
- rembg
- Pillow

## Usage

1. Run the Streamlit app with the command `streamlit run app.py`.
2. Upload an image using the file uploader.
3. Choose your desired background color using the color picker.
4. The app will display the original image and the processed image side by side.
5. Download the processed image by clicking the "Download Image" button.

## Future Enhancements

- Adding additional filters and effects.
- Implementing zoom and pan functionality.
- Supporting batch processing for multiple images.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [rembg](https://github.com/danielgatis/rembg)
- [Pillow](https://python-pillow.org/)
