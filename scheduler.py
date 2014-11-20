import time

import sys
print(sys.version)

weekdays = {
	'mon': 'Monday',
	'tue': 'Tuesday',
	'wed': 'Wednesday',
	'thu': 'Thursday',
	'fri': 'Friday',
	'sat': 'Saturday',
	'sun': 'Sunday'
}

class Class:
	department = ''
	number = ''
	days = []
	start_time = None
	end_time = None

	def __str__(self):
		days_of_week = ''
		for day in self.days:
			days_of_week = days_of_week + weekdays[day] + ', '
		days_of_week = days_of_week[0:-2]

		return self.department + ' ' + self.number + '\n' + \
			' on ' + days_of_week + '\n' + \
			' from ' + time.strftime("%I:%M %p", self.start_time) + '\n' + \
			' to ' + time.strftime("%I:%M %p", self.end_time)

def add_course():
	print("\nEnter the department designator")
	department = input("e.g. EECS or MATH: ") or 'EECS'

	print("\nEnter the class number")
	class_num = input("e.g. 325 or 470M: ") or '325'

	print("\nEnter what days the class is scheduled separated by commas")
	print("using these three letter designations: mon,tue,wed,thu,fri,sat,sun")
	days_str = input("e.g. mon,wed,fri or tue,wed: ") or 'mon,wed'
	days = days_str.split(',')

	while not set(days) <= set(weekdays.keys()):
		print("\nI got", days)
		print("Check your input")
		days = input("e.g. mon,wed,fri or tue,thu: ").split(',')

	same_time = input("\nDoes the class take place at the same time every day? [y/n]: ") or 'y'

	while same_time not in ['y', 'n']:
		same_time = input("\nAnswer must be y or n: ")

	if same_time == 'y':
		new_class = Class()
		new_class.department = department
		new_class.number = class_num
		new_class.days = days

		print("\nWhat time does it start? [h:mm pm/am]")
		start_time_str = input("e.g. 2:30 pm or 10:45 am: ") or '2:00 pm'
		new_class.start_time = time.strptime(start_time_str, "%I:%M %p")

		print("\nWhat time does it end? [h:mm pm/am]")
		end_time_str = input("e.g. 2:30 pm or 10:45 am: ") or '3:00 pm'
		new_class.end_time = time.strptime(end_time_str, "%I:%M %p")

		return [new_class]

	elif same_time == 'n':
		new_classes = {}

		for day in days:
			new_classes[day] = Class()
			new_classes[day].department = department
			new_classes[day].number = class_num
			new_classes[day].days = [day]

			print("\nWhat time does %s's class start? [h:mm pm/am]" % weekdays[day])
			start_time_str = input("e.g. 2:30 pm or 10:45 am: ") or '2:00 pm'
			new_classes[day].start_time = time.strptime(start_time_str, "%I:%M %p")

			print("\nWhat time does %s's class end? [h:mm pm/am]" % weekdays[day])
			end_time_str = input("e.g. 2:30 pm or 10:45 am: ") or '3:00 pm'
			new_classes[day].end_time = time.strptime(end_time_str, "%I:%M %p")

		return new_classes.values()

	else:
		print("\nWHAT DID YOU DO!?!?!?")

def main():
	classes = []
	while True:
		add_new = input("\nDo you want to add a new class? [y/n]: ") or 'y'
		while add_new not in ['y', 'n']:
			add_new = input("\nAnswer must be y or n: ")

		if add_new == 'n':
			print()
			for c in classes:
				print(c)

			sys.exit()

		classes.extend(add_course())

if __name__ == "__main__":
	main()
