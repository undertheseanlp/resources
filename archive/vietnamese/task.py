import os


def check_is_in_correct_directory():
    folder = os.getcwd()
    print(os.getcwd())
    if "setup.py" not in os.listdir(folder):
        print("[ERROR] Bạn cần vào thư mục `vietnamese`")
        exit(1)
