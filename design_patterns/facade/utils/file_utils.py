class FileUtils:
    def save_file(self, filename: str, content: str) -> None:
        with open(filename, 'w') as f:
            f.write(content)
