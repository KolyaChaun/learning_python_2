import time
import requests
import os
import threading
from multiprocessing import Process
from pathlib import Path
from cryptography.fernet import Fernet


# CPU-bound task (heavy computation)
def encrypt_file(path: Path):
    print(f"Processing file from {path} in process {os.getpid()}")
    key = Fernet.generate_key()

    with open("filekey.key", "wb") as filekey:
        filekey.write(key)

    with open("filekey.key", "rb") as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open("rockyou.txt", "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("rockyou.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted)


# I/O-bound task (downloading image from URL)
def download_image(image_url):
    print(
        f"Downloading image from {image_url} in thread {threading.current_thread().name}"
    )
    response = requests.get(image_url)
    with open("image.jpg", "wb") as f:
        f.write(response.content)


def main():
    try:
        time_start = time.perf_counter()
        file: Path = Path("rockyou.txt")

        encrypt_start = time.perf_counter()
        encrypt_process: Process = Process(target=encrypt_file, args=(file,))
        encrypt_process.start()

        download_start = time.perf_counter()
        download_thread: threading.Thread = threading.Thread(
            target=download_image, args=("https://picsum.photos/1000/1000",)
        )
        download_thread.start()

        download_thread.join()
        encrypt_process.join()

        encrypt_end = time.perf_counter()
        download_end = time.perf_counter()

        total = time.perf_counter() - time_start
        encryption_counter = encrypt_end - encrypt_start
        download_counter = download_end - download_start

        print(
            f"Time taken for encryption task: {encryption_counter}, I/O-bound task: {download_counter}, Total: {total} seconds"
        )
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
