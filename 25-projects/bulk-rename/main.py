import os

def main():
    path = "E:/images/"

    if not os.path.exists(path):
        print(f"Error: The folder '{path}'' does not exist.")
        return

    files = os.listdir(path)

    for file in files:
        name, ext = os.path.splitext(file)

        if ext.lower() == ".png" and name.isdigit():
            new_name = f"image{name}{ext}"
            old_path = os.path.join(path, file)
            new_path = os.path.join(path, new_name)

            print(f"Renaming '{file}' to '{new_name}'")

            try:
                os.rename(old_path, new_path)
            except OSError as e:
                print(f"Error renaming {file}: {e}")
        else:
            print(f"Skipping: {file}")

if __name__ == "__main__":
    main()
