import os
import subprocess

def install_dependencies():
    packages_dir = os.path.join(os.path.dirname(__file__), 'packages')
    requirements_file = os.path.join(os.path.dirname(__file__), 'requirements.txt')

    if not os.path.exists(packages_dir):
        print("Packages directory not found.")
        return

    if not os.path.exists(requirements_file):
        print("Requirements file not found.")
        return

    pip_install_cmd = [
        'pip', 'install', '--no-index', '--find-links', packages_dir, '-r', requirements_file
    ]

    try:
        subprocess.check_call(pip_install_cmd)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")

if __name__ == "__main__":
    install_dependencies()
