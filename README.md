# My Social Media App

This is a social media application built with Django. Users can create posts, upload images, like, comment, and share posts. The application also supports user profiles with profile pictures and bios.

## Project Structure

## Features

- User authentication and authorization
- Create, edit, and delete posts
- Upload images with posts
- Like, comment, and share posts
- User profiles with profile pictures and bios

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/my_social_media_app.git
    cd my_social_media_app
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

7. Open your browser and go to `http://127.0.0.1:8000/`.

## Usage

- Register a new user or log in with an existing account.
- Create a new post by filling out the form on the home page.
- View and interact with posts on the home page.
- Visit user profiles to see their posts and profile information.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.