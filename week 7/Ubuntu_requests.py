"""
Ubuntu-Inspired Image Fetcher
"I am because we are"

This program fetches an image from a given URL and stores it in a shared folder
called 'Fetched_Images'. Inspired by Ubuntu principles: community, respect,
sharing, and practicality.
"""

import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image(url: str):
    # Ensure directory exists
    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    try:
        # Connect to the "global community" of the internet
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check for HTTP errors

        # Extract filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no filename, generate one
        if not filename:
            filename = "downloaded_image.jpg"

        save_path = os.path.join(folder, filename)

        # Save in binary mode
        with open(save_path, "wb") as f:
            f.write(response.content)

        print(f"✅ Image fetched and saved as: {save_path}")

    except requests.exceptions.RequestException as e:
        # Respectful error handling
        print("⚠️ Could not fetch image. Please check the URL or your connection.")
        print(f"Error details: {e}")
    except Exception as e:
        print("⚠️ An unexpected error occurred.")
        print(f"Error details: {e}")


if __name__ == "__main__":
    try:
        url = input("🌍 Enter the image URL: ").strip()
        if not url:
            print("⚠️ No URL provided. Exiting respectfully.")
            sys.exit(1)

        fetch_image(url)
    except KeyboardInterrupt:
        print("\n👋 Program exited respectfully by user.")
