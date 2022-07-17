import argparse
from typing import Dict

from books.app import app
from fastapi.testclient import TestClient


def get_generated_openapi() -> Dict:
    client = TestClient(app)

    resp = client.get('/openapi.yaml')
    resp.raise_for_status()

    return resp.text


def save_generated_openapi(openapi: str, dest_path: str):
    with open(dest_path, 'w') as fp:
        fp.write(openapi)


def generate():
    parser = argparse.ArgumentParser(description='Generate OpenAPI schema from code.')
    parser.add_argument(
        'dest_path', type=str, help='Where to store the generated openapi.'
    )

    args = parser.parse_args()

    openapi = get_generated_openapi()
    save_generated_openapi(openapi, args.dest_path)
