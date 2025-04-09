# rswaves

## Setting Up the Development Environment

1. Install Homebrew, a package manager for macOS, by running the following command in the terminal:
    ```sh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install Python using Homebrew by running the following command:
    ```sh
    brew install python
    ```

3. Verify the installation by checking the Python version:
    ```sh
    python3 --version
    ```

4. Install a virtual environment tool, such as `venv`, by running the following command:
    ```sh
    python3 -m venv myenv
    ```

5. Activate the virtual environment:
    ```sh
    source myenv/bin/activate
    ```

6. Install necessary Python libraries for AI and music generation using `pip`:
    ```sh
    pip install tensorflow torch magenta music21 pyqt5 numpy scipy mido pretty_midi
    ```

7. Create a `requirements.txt` file to list all installed dependencies:
    ```sh
    pip freeze > requirements.txt
    ```

8. Download all dependencies listed in `requirements.txt` for offline use:
    ```sh
    pip download -r requirements.txt -d ./packages
    ```

9. Package the `requirements.txt` file and the `packages` directory together with your application code.

10. Ensure your application code includes a script to install the dependencies from the `packages` directory when running offline.

## Running the App

1. Activate the virtual environment:
    ```sh
    source myenv/bin/activate
    ```

2. Install the dependencies from the `packages` directory:
    ```sh
    python download_dependencies.py
    ```

3. Run the app:
    ```sh
    python main.py
    ```

The app will open a window with a user interface created using PyQt. You can generate, play, and save music using the provided buttons and sliders.
