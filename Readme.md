# Slideshow Web Viewer

Slideshow Web Viewer is a lightweight web application designed to render and display PDFs as slideshows directly in a web browser. This project eliminates the need for desktop software, providing a seamless way to view presentations online.

## Build and Deploy with Docker

1. Clone the repository:
    ```bash
    git clone https://github.com/albertsonblake/slides-web-viewer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd slides-web-viewer
    ```
3. Build the Docker image:
    ```bash
    docker build -t slides-web-viewer .
    ```
4. Run the Docker container:
    ```bash
    docker run -p {PORT}:8000 slides-web-viewer
    ```
5. Open your browser and navigate to `http://{host}:{PORT}` to access the application.

### Revesre Proxy

Highly recommended to use a reverse proxy like Caddy or Traefik to handle SSL termination and routing. This will ensure that your application is secure and can be accessed over HTTPS.

## Usage

1. Open your browser and navigate to `http://{host}:{PORT}`.
2. Upload a `.pdf` file using the provided interface.
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
