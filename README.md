# Wabbajack_download
A Python script to bypass the Nexus API limit on mod downloads when using Wabbajack.exe

Free Nexus Mods accounts have a download limit when using the official API. This script is designed to overcome that restriction by automating the process, making it ideal for large modpacks—such as those for Skyrim with over 4,000 mods—where manually clicking through each download would be impractical.

In short, this is a local script that automates clicking for you.

# Setup Instructions  

To run this script on a new PC, follow these steps:

    1. Install Python from https://www.python.org/downloads/.  
       - During installation, check the box **"Add Python to PATH"**.  

    2. Install the required packages by running:  
       ```
       pip install pyautogui pillow
       ```

    3. Verify the installation by running:  
       ```
       python -m pip list
       ```
       - Ensure `pyautogui` and `pillow` are listed.  

    4. Prepare the script:  
       - You must have an exact image of the "Slow Download" button saved as slow_download.png in the same directory as            the script.
       - Place this image in the same directory as the script.  

    5. Run the script:  
       ```
       python your_script.py
       ```
       - Replace `your_script.py` with the actual filename.  

    6. Additional Notes:  
       - If you get permission errors, try running the terminal as **Administrator**.  
       - If `pyautogui` does not work properly, ensure your **screen resolution scaling** is set to 100%.  

Your script should now work as expected!
