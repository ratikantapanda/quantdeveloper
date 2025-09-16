from .string_utils import StringUtils
from .math_utils import MathUtils
from .file_utils import FileUtils

# Handle orchestration
class UtilityFacade:
    def __init__(self):
        self.string_utils = StringUtils()
        self.math_utils = MathUtils()
        self.file_utils = FileUtils()

    def process_and_save(self, text: str, numbers: list, filename: str):
        cleaned = self.string_utils.clean_text(text)
        mean = self.math_utils.calculate_mean(numbers)
        result = f"{cleaned} has mean {mean}"
        self.file_utils.save_file(filename, result)
        return result
