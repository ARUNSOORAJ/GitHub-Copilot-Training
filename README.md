# OpenCV Image Processing Pipeline

This project demonstrates a simple pipeline for converting RGB images to grayscale using OpenCV.

## Project Structure

```
opencv-pipeline
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── image_processing.py  # Contains image processing functions
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Requirements

To run this project, you need to install the required dependencies. You can do this by running:

1. Create a virtual environment:

```
python -m venv venv
```

2. Activate the virtual environment:

- On Windows:
```
venv\Scripts\activate
```

- On macOS and Linux:
```
source venv/bin/activate
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Place your RGB image in the appropriate directory.
2. Run the main application:

```
python src/main.py
```

3. The resulting grayscale image will be saved or displayed based on the implementation in `main.py`.

## License

This project is licensed under the MIT License.