# MCP Weather Python
A simple MCP server to gather weather data from Open Weather.  This project is written in Python and uses the `mcp` library.

## Setup

### Using this Repository
Clone locally:
```sh
cd your_local_path
git clone https://github.com/tylerkempton/mcp-weather-python.git
```

### Creating from Scratch
Instructions for downloading and installing `python` can be found at [python.org](https://www.python.org/).

This project uses `uv` for project and package management.

Install `uv`:
```sh
pip install uv
```

Initialize the project:
```sh
uv init mcp-weather-python
```
Generate and activate the virtual environment:
```
uv venv
source .venv/bin/activate
```

Install dependencies.
```
uv add "mcp[cli]"
uv add "requests"
uv sync
```

Commit the newly created project files:
```
cd ./mcp-weather-python
git add .
git commit -m "Initial project creation."
```

### Open Weather
This project uses data from Open Weather obtained by calling their APIs.
1. Create an account and/or sign in at:
	- [https://openweathermap.org](https://openweathermap.org)
2. Generate an API key.

## Run
Test the weather MCP server with the MCP Inspector and Claude Desktop.

### MCP Inspector
1. Run your serer with the MCP Inspector, execute the following command:
	```sh
	mcp dev src/server.py
	```
2. Verify the output for the local address.
	- Should look like the following:
		```
		Starting MCP inspector...
		⚙️ Proxy server listening on 127.0.0.1:xxxx
		```
3. Click the link to "open inspector with token pre-filled". This will give you a UI you can use to test the MCP server in your browser.
