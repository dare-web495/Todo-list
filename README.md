# Todo List Application

This is a simple web-based Todo List application built using Flask, a lightweight web framework for Python. The application allows users to create, view, and delete items from their todo list.

## Features

- **Add Todo Items**: Users can enter new tasks into the todo list.
- **View Todo List**: All added tasks are displayed in a list format.
- **Delete Todo List**: Users can clear all tasks with a single button.

## Technologies Used

- **Python**: The backend logic is implemented using Python.
- **Flask**: The web framework used to handle requests and render templates.
- **HTML/CSS**: The frontend is built using HTML and styled with Bootstrap for responsive design.

## File Structure
/todo
│
├── app.py # Main application file
├── templates/
│ └── index.html # HTML template for rendering the todo list
└── static/
└── styles.css # Custom styles (if any)

## Installation

1. **Clone the repository**: <https://github.com/dare-web495/todo-list.git>
2. **Set up a virtual environment (optional but recommended)**: python -m venv venv source venv/bin/activate # On Windows use 'venv\Scripts\activate'
3. **Install Flask**: pip install Flask
4. **Run the application**: python app.py
5. **Access the application**: Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- To add a new todo item, enter the task in the input field and click the "Create" button.
- The current todo list will be displayed below the input field.
- To delete all items from the list, click the "New todo list" button.

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.


