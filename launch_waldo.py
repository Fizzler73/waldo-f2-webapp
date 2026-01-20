import subprocess
import os
import sys

# Get the path to this script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Full path to your app
app_path = os.path.join(current_dir, "app.py")

# Launch the Streamlit app
try:
    subprocess.run(["streamlit", "run", app_path], check=True)
except FileNotFoundError:
    print("Streamlit is not installed or not in PATH.")
    print("Please install it with: pip install streamlit")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print("Streamlit failed to launch.")
    sys.exit(e.returncode)
