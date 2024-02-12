import subprocess
import sys

# Function to install a package using pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def main():
    try:
        # Check if Python 3 is installed
        subprocess.run(["python3", "--version"], check=True)
        print("Python 3 is already installed.")
    except subprocess.CalledProcessError:
        # If Python 3 is not installed, install it
        print("Installing Python 3...")
        install("python3")
        print("Python 3 has been installed successfully.")

    try:
        # Check if pip is installed
        subprocess.run(["pip3", "--version"], check=True)
        print("pip is already installed.")
    except subprocess.CalledProcessError:
        # If pip is not installed, install it
        print("Installing pip...")
        install("python3-pip")
        print("pip has been installed successfully.")

    try:
        # Check if Pandas is installed
        import pandas
        print("Pandas is already installed.")
    except ImportError:
        # If Pandas is not installed, install it
        print("Installing Pandas...")
        install("pandas")
        print("Pandas has been installed successfully.")

    print("\nInstallation completed.")

    # Instructions for creating and activating a virtual environment (optional)
    print("\nFor creating and activating a virtual environment, you can run the following commands:")
    print("\n1. Install virtualenv (if not already installed):")
    print("   sudo apt install python3-venv")
    print("\n2. Create a virtual environment:")
    print("   python3 -m venv myenv")
    print("\n3. Activate the virtual environment:")
    print("   source myenv/bin/activate")
    print("\nAfter activation, you can install additional packages using pip, which will be isolated to this virtual environment.")

# Entry point of the script
if __name__ == "__main__":
    main()
