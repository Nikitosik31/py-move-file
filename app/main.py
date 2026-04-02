import os


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "mv":
        return

    mv, source, destination = parts
    if destination.endswith("/"):
        dir_path = destination[:-1]
        file_name = source
    else:
        dir_path, file_name = os.path.split(destination)

    current_path = ""
    if dir_path:
        parts = dir_path.split("/")
    else:
        parts = []

    for part in parts:
        if current_path == "":
            current_path += part
        else:
            current_path = current_path + "/" + part

        if not os.path.exists(current_path):
            os.mkdir(current_path)

    if dir_path:
        full_path = dir_path + "/" + file_name
    else:
        full_path = file_name

    with open(source, "r") as f1, open(full_path, "w") as f2:
        f2.write(f1.read())
        os.remove(source)
