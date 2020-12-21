# Flight Deal Finder - Capstone Part 1

## Step 1 
- Download the starting project

Unzip the downloaded file and open the project in PyCharm.

Take a look through the starting project to get a sense for the structure of the final program.

## Step 2
- Chose Your Path  

You can chose to build the project entirely yourself or you can follow step-by-step challenges.  

If you feel you are an advanced programmer and you have learnt and understood all the concepts in the course so far (OOP, APIs, datetime, List and Dictionary Comprehensions) then stop here and try to create the project yourself using the APIs listed below.  

- Make Your Own Copy of the Starting Google Sheet: [sheets](https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit?usp=sharing)

### APIs Required:

- [Google Sheet Data Management](https://sheety.co/)

- [Flight Search API](https://partners.kiwi.com/)

- [Flight Search API Documentation](https://tequila.kiwi.com/portal/docs/tequila_api)

- [Twilio SMS API](https://www.twilio.com/docs/sms)

## Program Requirements:

Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code, not the airport code.

Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

If the price is lower than the lowest price listed in the Google Sheet then send a SMS to your own number with the Twilio API.

The SMS should include:
- the departure airport IATA code
- destination airport IATA code
- departure city 
- destination city
- flight price
- flight dates

## Step 3
- Get the IATA Codes

In order to search for flights we need an International Air Transport Association (IATA) code. This code helps to identify airports and metropolitan areas.

Some airports are so famous that people even refer to the IATA code in normal conversation. e.g LAX and JFK.

Some cities have multiple airports, so they have their own city IATA code which is different from the airport IATA code. e.g. LON (London) - LHR (Heathrow)/ LGW(Gatwick) etc.

The goal for this step is to add the missing IATA codes for each city to the Google Sheet.

### Step 4 
- Search for Cheap Flights

The next step is to search for the flight prices from London (LON) to all the destinations in the Google Sheet.

We're looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time. We're looking for round trips that return between 7 and 28 days in length. The currency of the price we get back should be in GBP.

Take a look at the Flight Search API to see which parameters you can pass to the API:
[tequila api](https://tequila.kiwi.com/portal/docs/tequila_api/search_api)

## Step 5 
- If Flight Price Lower than in Google Sheet send an SMS
The final step is to check if any of the flights found are cheaper than the Lowest Price listed in the Google Sheet. If so, then we should use the Twilio API to send an SMS with enough information to book the flight. You should use the NotificationManager for this job.

Message should Include:

```
Price
Departure City Name
Departure Airport IATA Code
Arrival City Name
Arrival Airport IATA Code
Outbound Date
Inbound Date
```
