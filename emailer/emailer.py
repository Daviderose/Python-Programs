import requests
import smtplib

def get_emails():
	'''pulls in emails from email list.txt and returns them in a dictionary.'''
	emails = {}		# Create empty dictionary

	try:			# Open email list, catch error if unable 
		email_file = open('email list.txt', 'r')
		for email in email_file:
			(email, name) = email.split(',')
			emails[email] = name.strip()

	except FileNotFoundError as err:
		print(err)

	return emails	# Return list as filled emails dictionary

def get_weather_forecast():
	'''uses open weather API to gather weather data and returns forecast.'''

	# Request weather JSON data from open weather API
	url = 'http://api.openweathermap.org/data/2.5/weather?zip=63105,us&units=imperial&appid=c8df1fa1128eae37b4e75387b8e82eb8'
	weather_request = requests.get(url)
	weather_json = weather_request.json()

	# Pull out relevant data from JSON dictionary
	description = weather_json['weather'][0]['description']
	temp_min = weather_json['main']['temp_min']
	temp_max = weather_json['main']['temp_max']

	# Build and return forecast in a string
	forecast = 'The forecast for St. Louis today is '+ description + ', with a min temperature of ' 
	forecast += str(int(temp_min)) + ' and a max temperature of ' + str(int(temp_max)) + '.'

	return forecast

def send_emails(emails, forecast):
	# Connect to SMTP server
	server = smtplib.SMTP('smtp.gmail.com', '587')

	# Start TLS encryption
	server.starttls()

	# Login
	from_email = 'daviderose526@gmail.com'
	password = input('What is your password?')
	server.login(from_email, password)

	# Send email to entire email list
	for to_email, name in emails.items():
		message = "Subject: Today's weather forecast\n"
		message += 'Hi ' + name + '!\n\n'
		message += forecast + '\n\n'
		message += 'Have a great day no matter the weather!' + '\n\n'

		server.sendmail(from_email, to_email, message)
	
	server.quit()

def main():

	emails = get_emails()
	forecast = get_weather_forecast()
	
	send = send_emails(emails, forecast)

if __name__ == '__main__':
    main()