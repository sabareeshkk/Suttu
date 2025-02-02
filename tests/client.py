import http.client

# Set up the connection to the server
conn = http.client.HTTPConnection("localhost", 8080)

# Prepare the data to send in chunks
data_chunks = [
    b"5\r\nHello\r",    # First chunk: "Hello"
    b"\n8\r\n, world!\r\n", # Second chunk: ", world!"
    b"0\r\n\r\n"          # End of chunks (chunk size 0)
]

# Prepare headers
headers = {
    "Content-Type": "application/json",
    "Transfer-Encoding": "chunked",
    "Host": "localhost:8080"
}

# Start the HTTP request
conn.request("POST", "/upload", headers=headers)

# Send the body in chunks
for chunk in data_chunks:
    conn.send(chunk)  # Send each chunk one by one

# Get the response from the server
response = conn.getresponse()
print(f"Response status: {response.status}")
print(f"Response reason: {response.reason}")
print(f"Response body: {response.read().decode()}")

# Close the connection
conn.close()
