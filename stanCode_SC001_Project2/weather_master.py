"""
File: weather_master.py
Name: Ryan Chung
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This number controls when to stop the program
SECRET = -100


def main():
	print("stanCode \"Weather Master 4.0\"!")
	temperature = int(input('Next Temperature: (or '+str(SECRET)+' to quit)?'))
	if temperature == SECRET:
		print('No temperatures were entered.')
	else:
		highest = temperature
		lowest = temperature
		count = 1
		sum_temperatures = temperature
		if temperature < 16:
			cold_day = 1
		else:
			cold_day = 0
		while True:
			temperature = int(input('Next Temperature: (or -100 to quit)? '))
			if temperature == SECRET:
				break
			if highest < temperature:
				highest = temperature
			if lowest > temperature:
				lowest = temperature
			count += 1
			sum_temperatures += temperature
			if temperature < 16:
				cold_day += 1
		if count == 0:
			average = temperature
		else:
			average = sum_temperatures / count

		print('Highest temperature = ' + str(highest))
		print('lowest temperature = ' + str(lowest))
		print('Average =', average)
		print(cold_day, 'cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == "__main__":
	main()
