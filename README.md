# Suttu

## Installation
To install the `Suttu` package from TestPyPI, run the following command:

```sh
pip install -i https://test.pypi.org/simple/ Suttu
```

## Usage
Here is an example of how to use `Suttu` in a simple web application:

```python
from Suttu import Suttu, request
from werkzeug.serving import run_simple

app = Suttu()

@app.route("/hello", methods=["GET"])
def users():
    print(request)
    return request.data

if __name__ == "__main__":
    run_simple("localhost", 8000, app)
```

## Running the Application
After running the script, start the server with:

```sh
python your_script.py
```

Then, open your browser and navigate to:

```
http://localhost:8000/hello
```

## License
This project is licensed under the MIT License.

