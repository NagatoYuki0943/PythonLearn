import base64

# Define the string to be encoded
string = "Hello, World!"

# Encode the string using Base64
encoded_string = base64.b64encode(string.encode("utf-8"))

# Print the encoded string
print("Encoded string:", encoded_string)
# Encoded string: b'SGVsbG8sIFdvcmxkIQ=='

# Decode the encoded string
decoded_string = base64.b64decode(encoded_string).decode("utf-8")

# Print the decoded string
print("Decoded string:", decoded_string)
# Decoded string: Hello, World!
