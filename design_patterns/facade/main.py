from utils import UtilityFacade

facade = UtilityFacade()

result = facade.process_and_save(
    text="   Hello World!   ",
    numbers=[10, 20, 30],
    filename="output.txt"
)

print(result)


