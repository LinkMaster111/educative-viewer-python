## educative-viewer-python

### Overview

This project is a simple web application built using Flask that allows users to browse and open HTML files. The application uses Tailwind CSS for styling and provides a settings option to change the base directory dynamically. Users can load any Educative course from Tutflix that contains a `__toc__.json` file, set the base directory, and explore the course contents.

Disclaimer: This project is for educational purposes only and does not intend to break any copyright laws. Please ensure you have the legal right to access and use any course content you browse through this application.

### Features

- Browse and open HTML files in a structured format.
- Dynamically change the base directory using a settings modal.
- Tailwind CSS for a dark theme interface.
- Exportable as a standalone executable for easy sharing and use.

### Prerequisites

- Python 3.10 or higher.
- `Flask` and other dependencies listed in `requirements.txt`.

### Installation and Usage

#### Running the Standalone Executable

1. **Download the Executable**:
   Obtain the standalone executable file (e.g., `app.exe` if built using PyInstaller) from the `dist` directory or as provided.

2. **Run the Executable**:
   - On Windows:
     Simply double-click the `app.exe` file.
   - On macOS and Linux:
     Open the terminal and navigate to the directory containing the executable. Run it with:
     ```bash
     ./app
     ```

3. **Open the Application in a Browser**:
   Go to `http://127.0.0.1:5000/` in your web browser.

#### Running the Project Using Virtual Environment (venv)

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LinkMaster111/educative-viewer-python.git
   cd educative-viewer-python
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Download Tailwind CSS**:
   Make sure the `tailwind.min.css` file is in the `static` directory.
   
   **Example Directory Structure**:
   ```
   my_flask_app/
   ├── app.py
   ├── static/
   │   └── tailwind.min.css
   |   └── educative.svg 
   ├── templates/
   │   └── index.html
   ├── requirements.txt
   └── README.md
   ```

6. **Run the Flask Application**:
   ```bash
   python app.py
   ```

7. **Open the Application in a Browser**:
   Go to `http://127.0.0.1:5000/` in your web browser.


### Instructions for Using the Application

1. **Get an Educative Course**:
   Download any Educative course from Tutflix. Ensure the modules have a `__toc__.json` file that contains the table of contents.

2. **Set the Base Directory**:
   - Copy the path to the course directory. It should look similar to this:
     ```
     C:\Users\USER_NAME\Downloads\Courses\Educative-77 in Java_ Accelerate Your Coding Interview Prep
     ```
   - Run the project and click on the settings icon at the top right corner of the application.

3. **Enter the Base Directory**:
   - In the settings modal that appears, paste the copied path into the "Base Directory" field.
   - Click "Save" to set this as the base directory.

4. **Browse and Open Files**:
   The application will automatically load the files from the specified directory. You can now browse and open the files directly from the web interface.


### Troubleshooting

- **CSS Not Loading**:
  Ensure the `tailwind.min.css` file is placed correctly in the `static` directory and referenced properly in your HTML using Flask’s `url_for` method.

- **Executable Not Running**:
  Make sure all dependencies and files are correctly bundled in the executable. If using PyInstaller, ensure to include all necessary data files (CSS, templates) with the `--add-data` option.
