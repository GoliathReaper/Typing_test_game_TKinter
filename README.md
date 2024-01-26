# Typing Test CustomTkinter GUI Application
### Overview
This is a simple Typing Test GUI application built using the customtkinter library, a customized version of the Tkinter library. The application measures the user's typing speed (in words per minute - WPM) and accuracy within a specified time limit. The user is presented with a passage to type, and their input is compared against the actual text to calculate performance metrics.

### Features
* User-friendly GUI interface.
* Ability to start and restart the typing test.
* Real-time timer display.
* Measurement of WPM (Words Per Minute) and accuracy.

### Getting Started
To run the application, ensure you have the necessary dependencies installed:

```bash
pip install customtkinter
```

After installing the dependencies, execute the script. The GUI window will appear, and you can start the typing test by clicking the "Start" button. To restart the test, click the "Restart" button.

### Usage
1. Launch the application.
2. Click the "Start" button to initiate the typing test.
3. Type the displayed text into the input box.
4. Once the timer reaches zero, the test will automatically stop.
5. View your results, including WPM and accuracy.

### Code Structure
* The application is structured in a modular manner with functions for starting, restarting, and updating the timer.
* The get_text function continuously monitors the user's input for real-time performance evaluation.
* The score function calculates WPM and accuracy based on the user's input.

### Customization
* The appearance mode and color theme of the GUI can be customized using the customtkinter library functions.
* The default appearance mode is "System," and the default color theme is "blue."

### Dependencies
* customtkinter
* random

### Notes
The actual text for typing is randomly selected from a predefined list in the data module.
Feel free to explore and modify the code according to your preferences or requirements. Happy typing!
