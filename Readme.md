# Slideshow Web Viewer

Slideshow Web Viewer is a lightweight web application designed to render and display PDFs as slideshows directly in a web browser. This project eliminates the need for desktop software, providing a seamless way to view presentations online.

## Build and Deploy with Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pptx-web-viewer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd pptx-web-viewer
    ```
3. Build the Docker image:
    ```bash
    docker build -t pptx-web-viewer .
    ```
4. Run the Docker container:
    ```bash
    docker run -p 8000:8000 pptx-web-viewer
    ```
5. Open your browser and navigate to `http://localhost:8000` to access the application.

## Usage

1. Open your browser and navigate to `http://localhost:3000`.
2. Upload a `.pptx` file using the provided interface.
3. View and navigate through the presentation slides.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```bash
    git checkout -b feature-name
    ```
3. Commit your changes:
    ```bash
    git commit -m "Add feature-name"
    ```
4. Push to your branch:
    ```bash
    git push origin feature-name
    ```
5. Open a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Built with ❤️ by [Your Name/Team].
- Powered by modern web technologies.
