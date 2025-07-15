import random
from datetime import datetime, timedelta
import sqlite3  

# Connect to the database
connection = sqlite3.connect('SeniorProject.db')  
cursor = connection.cursor()

# Provinces
# provinces = [
#     "ab", "bc", "mb", "nb", "ns", "nt", "on", "qc", "sk"
# ]

# Event names, types, and creators
event_names = [
    'Tech Expo', 'Green Energy Conference', 'Annual Gala', 'Music Festival', 'Art Fair',
    'Business Summit', 'Health Workshop', 'Education Forum', 'Innovation Conference', 'Cultural Expo',
    'Food and Wine Festival', 'Startup Fair', 'Digital Marketing Meetup', 'International Book Fair',
    'Film Festival', 'Sustainable Future Summit', 'Gaming Convention', 'Sports and Wellness Expo',
    'Science and Technology Showcase', 'Community Volunteer Day', 'Fashion Week', 'Career Networking Night',
    'Youth Leadership Camp', 'Coding Bootcamp', 'Cybersecurity Seminar', 'AI Symposium', 'Literary Festival',
    'Local Farmers Market', 'Women in Tech Conference', 'Blockchain Summit'
]

event_types = [
    'Exhibition', 'Conference', 'Gala', 'Workshop', 'Forum', 'Festival',
    'Seminar', 'Meetup', 'Symposium', 'Showcase', 'Convention', 'Retreat',
    'Camp', 'Expo', 'Fair', 'Lecture', 'Panel', 'Competition', 'Networking Event'
]

creators = [
    'Alex Kim', 'Jamie Chen', 'Taylor Swift', 'Jordan Lee', 'Sam Morgan', 'Casey White',
    'Morgan Lee', 'Taylor Brown', 'Jordan White', 'Samantha Chen', 'Chris Young',
    'Jamie Nguyen', 'Michael O’Hara', 'Kim Tanaka', 'Parker Quinn', 'Jessie Anderson',
    'Logan Martinez', 'Chris Park', 'Riley Robinson', 'Avery James', 'Morgan Smith',
    'Dakota Green', 'Taylor Brooks', 'Jordan Carter', 'Madison Evans', 'Cameron Reed',
    'Quinn Bailey', 'Alex Johnson', 'Sam Lee', 'Riley Turner'
]

num_records = 50

# Date 
start_date_range = datetime(2022, 11, 1)
end_date_range = datetime(2023, 3, 31)

# Facility_names from the venue table
cursor.execute("SELECT ID, Facility_name FROM venue")
venue_data = cursor.fetchall()

data = []
for _ in range(num_records):
    
    venue_id, venue_name = random.choice(venue_data)
    while venue_name == "unknown":
        venue_id, venue_name = random.choice(venue_data)
        
    event_name = random.choice(event_names)
    start_date = start_date_range + timedelta(days=random.randint(0, (end_date_range - start_date_range).days))
    end_date = start_date + timedelta(days=random.randint(1, 5))
    event_type = random.choice(event_types)
    creator = random.choice(creators)
    number_of_audience = random.randint(1, 50)
    budget = random.randint(1000, 10000)


    data.append((event_name, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'),
             event_type, creator, number_of_audience, budget, venue_id))


cursor.executemany('''
    INSERT INTO user_event (Event_name, Start_date, End_date, Type_of_event, Creator, 
                            Number_of_audience, Budget, VenueID)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', data)

connection.commit()
connection.close()

print("Random data with budget and valid facility name was inserted successfully")

