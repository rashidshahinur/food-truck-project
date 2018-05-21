import requests
import smtplib
import datetime

def get_emails():
	# Better to be read in a dictionary because the email_list.txt has 2 separate parts email and name
	emails = {}

	# Get the user email list by opening the email_list.txt file
	# Use Try to avoid the program crashing from opening an invalid file
	try:
		email_file = open('email_list.txt', 'r')

		# Now I want to read each line in this file into the dict
		for line in email_file:
			# Separate email and name by a comma and the space by creating a tuple
			(email, name) = line.split(',')
			
			# Insert key-value pairs into the emails dict, also remove white space character on the name
			emails[email] = name.strip()
			
	except FileNotFoundError as err:
		print(err)

	return emails

def get_menu():
	print('This is our menu specials for today:')
	# Read the menu.txt file
	try:
		menu_file = open('menu.txt', 'r')
		menu = menu_file.read().strip()
		# ascii error occured when run, use encode to remove symbols and keep string as string
		menu = menu.encode('ascii', 'ignore').decode('ascii')
	except FileNotFoundError as err:
		print(err)

	return menu

# Get the weather data from the openweathermap.org/api website
def get_weather_forecast():
	# Import requests module at the top of this script
	# Connect to the weather api using the registered api key: &appid=f641b59e03463c808393605f493b1f93
	weather_request = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=94063,us&units=imperial&appid=f641b59e03463c808393605f493b1f93')
	weather_json = weather_request.json()

	# Parsing JSON
	description = weather_json['weather'][0]['description']
	temp_min = weather_json['main']['temp_min']
	temp_max = weather_json['main']['temp_max']

	# Create a string to return
	forecast = 'The weather forecast in Palo Alto for today is '
	forecast += description + ' with a high of ' + str(int(temp_max)) + ' and a low of ' + str(int(temp_min)) + '.'
	#±forecast = forecast.encode('ascii', 'ignore').decode('ascii')
	return forecast

def get_date():
	# Get today date using datetime package
	today = datetime.date.today()
	# Format the date using strftime
	today = today.strftime("%B %d, %Y")

	return today

# Use Gmail SMTP Settings to send emails to the app users
def send_emails(emails, menu, forecast, today):
	# Connect to the smtp server
	server = smtplib.SMTP('smtp.gmail.com', '587')

	# Start TSL enrcryption
	server.starttls()

	# Login gmail smtp server
	password = input("What is your password?") 
	from_email = 'thi.m.duong@gmail.com'
	server.login(from_email, password)

	# Send to entire email list
	for to_email, name in emails.items():
		message = 'Subject: Welcome to Banh Mi Sai Gon!!\n'
		message += 'Hi ' + name + '!\n\n'
		message += 'Thank you for signing up to our customer email list.\n\n'
		message += 'Our foodtruck is opened today ' + today + ' ' + 'from 11:00 AM to 3:00 PM at our regular location.\n\n'
		message += 'We have provided some information below for your convenience:\n\n'
		message += menu + '\n\n'
		message += "Today's weather forecast:\n" + '\n' + forecast + '\n\n'
		message += 'Hope to see you there!'
		server.sendmail(from_email, to_email, message)
	
	server.quit()


def main():
	emails = get_emails()
	print(emails)	
	menu = get_menu()
	print(menu)
	forecast = get_weather_forecast()
	print(forecast)
	today = get_date()
	print(today)
	send_emails(emails, menu, forecast, today)

main()