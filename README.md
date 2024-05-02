# Personal CAD File Change Control System
## Author: Alfredo Macias
## Contact: www.linkedin.com/in/alfredo-j-macias-952b55123

## Introduction
Welcome to the Personal CAD File Change Control System! This project integrates seamlessly with Trello to provide a sophisticated change control system tailored specifically for managing CAD file revisions. It is ideal for engineers, designers, and project managers who need to maintain an organized record of design changes and version history.

## Key Features
Our system boasts several standout features designed to simplify your workflow:

- **Trello Integration**: Automatically generate Trello cards for each new change request, linking your project management tools directly with change tracking.
- **Alphanumeric Revision Tracking**: Utilize a robust alphanumeric system that accurately tracks and logs each version of your CAD files, ensuring no detail is missed.
- **User-Friendly GUI**: Engage with a clean and intuitive graphical user interface that makes submitting and reviewing change requests a breeze.

## Getting Started
Follow these detailed steps to get the system up and running on your machine:

### Prerequisites
- Python 3.6 or higher
- Pip for Python package management

### Installation
1. **Clone the Repository**: Clone the source code to your local machine to get started with the setup:
   ```bash
   git clone https://github.com/yourusername/cad-file-change-control.git
   cd cad-file-change-control
   ```
2. **Install Dependencies**: Install the necessary Python modules using pip:
   ```bash
   pip install requests
   ```
3. **Configure Trello API Credentials**:
   - Navigate to [Trello's API Key page](https://trello.com/app-key) to obtain your API key and token.
   - Edit the configuration file `config.py`, replacing `API_KEY`, `TOKEN`, and `BOARD_ID` with your respective details.

### Running the Application
Execute the following command to start the application:
   ```bash
   python change_control.py
   ```
The GUI will prompt you to enter necessary details for tracking CAD file changes. Once you complete the form and submit, a new Trello card reflecting the change request is automatically created.

## Code Explanation
This section breaks down key parts of the source code to help you understand how the application functions:

### Trello API Integration
- **File**: `trello_integration.py`
- **Purpose**: Handles all interactions with the Trello API, including card creation and updates.
- **Key Functions**:
  - `create_card`: Takes parameters like file name, revision number, and change description to create a Trello card.
  - `update_card`: Used to update an existing card with new information or status changes.

### Alphanumeric Revision Tracking
- **File**: `revision_tracker.py`
- **Purpose**: Manages the tracking and updating of revision numbers for CAD files using an alphanumeric system.
- **Key Functions**:
  - `get_latest_revision`: Retrieves the latest revision number from the database.
  - `update_revision`: Updates the revision number in the database after changes are approved.

### GUI Implementation
- **File**: `gui.py`
- **Purpose**: Provides the graphical user interface for the application.
- **Key Components**:
  - `SubmissionForm`: A form where users can enter details about the CAD file changes.
  - `MainWindow`: The main window of the application that hosts all other GUI components.

## Usage Examples
Here are a few scenarios where our system can enhance your CAD file management:
- **Revision Submission**: Quickly submit revisions and modifications for CAD designs directly through the GUI.
- **Project Tracking**: Monitor the status of various changes and revisions through corresponding Trello cards.
- **Collaboration**: Share Trello cards with team members to improve communication and collaboration on projects.

## Contributing
We encourage contributions from the community! If you have suggestions for improvements or new features, please follow these steps:
- **Fork the Repository**: Fork the project to your GitHub account.
- **Create a Feature Branch**: Make your changes in a new branch named after the feature.
- **Submit a Pull Request**: Open a pull request for discussion and possible integration into the main branch.

## License
This project is licensed under the MIT License. For more details, see the LICENSE file included with the code.

## Contact
Should you have any questions or require further information, please open an issue in this repository, and we will respond promptly.
