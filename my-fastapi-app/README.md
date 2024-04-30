# My FastAPI App

This is a FastAPI application that includes a simple geoprocessing functionality for creating buffers using arcpy.

## Project Structure

```
my-fastapi-app
├── app
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── buffer_processing.py
│   ├── tests
│   │   └── test_buffer_processing.py
│   └── docs
│       └── api_documentation.md
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/my-fastapi-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd my-fastapi-app
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the FastAPI application:

   ```bash
   uvicorn app.main:app --reload
   ```

2. Open your web browser and navigate to `http://localhost:8000/docs` to access the API documentation.

## API Routes

- `POST /buffer`: Create a buffer using arcpy.

  Request Body:
  - `input_file`: File path of the input shapefile.
  - `output_file`: File path of the output shapefile.
  - `distance`: Buffer distance in the units of the input shapefile.

  Example Request:
  ```json
  {
    "input_file": "path/to/input.shp",
    "output_file": "path/to/output.shp",
    "distance": 100
  }
  ```

  Example Response:
  ```json
  {
    "message": "Buffer created successfully."
  }
  ```

## Testing

To run the unit tests for the buffer processing function, execute the following command:

```bash
pytest app/tests/test_buffer_processing.py
```

## Documentation

For detailed documentation of the API routes and their usage, please refer to [api_documentation.md](app/docs/api_documentation.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.