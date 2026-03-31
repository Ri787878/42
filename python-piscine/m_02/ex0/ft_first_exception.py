# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ridias <ridias@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/31 12:30:31 by ridias            #+#    #+#              #
#    Updated: 2026/03/31 13:09:18 by ridias           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def input_temperature(temp_str: str) -> int:
	number = int(temp_str, base=10)
	return number

def test_temperature() -> None:
	test1: str = "25"
	test2: str = "abc"
	try :
		print(f"Input data is '{test1}'")
		number1: int = input_temperature(test1)
		print(f"Temperature is now {number1}°C")
		print()
	except:
		print(f"Caught input_temperature error: invalid literal for int() with base 10: {test1}")
		print()
	try :
		print(f"Input data is '{test2}'")
		number2: int = input_temperature(test2)
		print(f"Temperature is now {number2}°C")
		print()
	except:
		print(f"Caught input_temperature error: invalid literal for int() with base 10: {test2}")
		print()
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
	print(f"=== Garden Temperature ===")
	print("")
	test_temperature()
