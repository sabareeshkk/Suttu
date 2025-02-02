# helper functions
from src.common import constants


def parse_headers(data):
    # get header and body
    headers, body = data.split(constants.REQ_HEADER_SEPERATOR)
    # split headers in to array
    header_arr = headers.split(constants.HEADER_SEPERATOR)
    # parse header
    http_req_header_metadata, http_req_header_data = header_arr[0], header_arr[1:]
    # parse header metadata
    http_metadata = parse_req_header_meta(http_req_header_metadata)
    # parse header data
    header_data = parse_req_header_values(http_req_header_data)
    return header_data | http_metadata

def parse_data(data):
    # get header and body
    body = data.split(constants.REQ_HEADER_SEPERATOR)[1]
    return body



def parse_req_header_meta(http_req_metadata):
    # Split the request line into parts
    method, path, http_version = http_req_metadata.decode().strip().split(" ")

    # Parse the HTTP version (if needed)
    http_version = http_version.split("/")[1]
    return {"method": method, "path": path, "http_version": http_version}

def parse_req_header_values(http_req_header_values):
    header_values = {}
    for req_buffer in http_req_header_values:
        head_key, head_value = req_buffer.decode().strip().split(": ")
        if head_key not in header_values:
            # TODO: need to parse values according to their types
            header_values[head_key] = head_value
    return header_values