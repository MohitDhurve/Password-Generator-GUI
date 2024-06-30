# Password-Generator-GUI
<p>This project is a GUI-based password generator that allows users to create secure passwords with customizable options such as length, inclusion of uppercase letters, lowercase letters, digits, and special characters.</p>
<h3>Table of Contents</h3>
<ol>
  <li>Installation</li>
  <li>Usage</li>
  <li>Code Structure</li>
  <li>Features</li>
  <li>Troubleshooting</li>
  <li>Contributing</li>
</ol>
<h3>Installation</h3>
<h4>Prerequisites</h4>
<ul>
  <li>Python: Make sure you have Python 3.x installed. Download it from <a href="https://www.python.org/downloads/">Python.org</a>.</li>
</ul>
<h4>Steps</h4>
<ol>
  <li>Clone the Repository
  </li>
  <li>Set Up a Virtual Environment (optional but recommended):
    <p>python -m venv venv <br>
      source venv/bin/activate   # On Windows use `venv\Scripts\activate`
</p>
  </li>
  <li>Install Required Libraries:
    <p>pip install tkinter<br>
    Note: tkinter is usually included with Python, so this step may not be necessary.
    </p>
    
  </li>
</ol>
<h3>Usage</h3>
<ol>
  <li>Run the Application:
  <p>python main.py
  </p>
  </li>
  <li>Using the GUI:
    <ul>
      <li>Enter the Password Length: Specify the desired length of the password.</li>
      <li>Select Character Options: Check the boxes to include uppercase letters, lowercase letters, digits, and special characters.</li>
      <li>Generate Password: Click the "Generate Password" button to create a password based on the selected criteria.</li>
      <li>View Password: The generated password will appear in the text box.</li>
    </ul>
  </li>
</ol>
<h3>Code Structure</h3>
<h4>`main.py`</h4>
<p>This is the main script that contains the following:</p>
<h5>Imports:</h5>
<ul>
  <li>`random`: For generating random characters.</li>
  <li>`string`: For character sets.</li>
  <li>`tkinter`: For creating the GUI.</li>
  <li>`messagebox`: For displaying error messages.</li>
</ul>
<h5>Functions:</h5>
<ul>
  <li>`generate_password(...)`: Generates a random password based on user specifications.</li>
  <li>`on_generate()`: Handles the password generation process when the button is clicked.</li>
</ul>
<h5>Main GUI Setup:</h5>
<ul>
  <li>Creates a `Tk` window with various input fields and buttons for user interaction.</li>
</ul>

<h3>Key Components</h3>
<ul>
  <li>Character Type Checkboxes: Allow users to select the types of characters to include in the password.</li>
  <li>Password Length Entry: Input field for the desired password length.
</li>
  <li>Password Display: Displays the generated password in a text box.</li>
</ul>

<h3>Features</h3>
<ul>
  <li>Customizable Password Length: Users can specify how long the password should be.</li>
  <li>Character Type Selection: Options to include/exclude uppercase, lowercase, digits, and special characters.</li>
  <li>Error Handling: Provides informative error messages for user inputs.</li>
  <li>Randomness: Ensures that each password generated is unique and random.</li>
</ul>

<h3>Troubleshooting</h3>
<h5>No Password Length Entered:</h5>
<ul>
  <li>Error: "Please enter the password length."</li>
  <li>Solution: Enter a numeric value in the password length field.</li>
</ul>
<h5>Password Length Too Short:</h5>
<ul>
  <li>Error: "Error: "Password length must be at least 4."</li>
  <li>Solution: Enter a length of 4 or more.</li>
</ul>
<h5>No Character Types Selected:</h5>
<ul>
  <li>Error: "Please select at least one character type."</li>
  <li>Solution: Ensure at least one checkbox for character types is selected.</li>
</ul>
<h5>Tkinter Installation Issues:</h5>
<ul>
  <li>Ensure Python and tkinter are properly installed on your system.</li>
</ul>

<h3>Contributing</h3>
<ol>
  <li>Fork the Repository.</li>
  <li>Create a Branch:</li>
  <li>Make Changes: Add your features or fix bugs.</li>
  <li>Commit Changes</li>
  <li>Push to Your Branch</li>
  <li>Create a Pull Request: Submit your changes for review.</li>
</ol>

<p>Feel free to customize the documentation as needed!</p>
