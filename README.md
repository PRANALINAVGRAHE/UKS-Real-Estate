# Real Estate Management System in Django

## Key Features:
1.Property Listing and Search: The system allows property owners and agents to list their properties, including detailed information, images, and amenities. Potential buyers can easily search and filter through the listings to find properties that meet their requirements.

2.User Accounts and Authentication: Users can create accounts and log in to access personalized features, ensuring a tailored experience for each user category.

3.Property Management: Property owners and agents can efficiently manage their properties through the system. They can update property details, availability status, and track inquiries.

4.Property Analytics: The system provides valuable data analytics and insights, helping users make informed decisions related to real estate investments and transactions.

5.Real-Time Communication: The platform facilitates real-time communication between property owners, agents, and potential buyers, improving collaboration and responsiveness.

6.Booking and Appointments: For rental properties, the system handles appointment scheduling and booking, streamlining the process for both tenants and property owners.

## Installation Guide
1.clone this repository using:

	`git clone https://github.com/reaganodhiambo/Django-eal-Estate.git`
	
2.set up a virtual environment(optional but recommended)

	`python -m venv venv`
	`source venv/bin/activate` #macOS or Linux
    `venv\Scripts\activate.bat`  # Windows

3.Install all required packages:

	`pip install -r requirements.txt`

4.Create a .env file to store your environment variables and add relevant info.

5.Migrate the database

	`python manage.py migrate`

6.Create a superuser to access the Django admin:

	'python manage.py createsuperuser`

7.Run the development server:

	`python manage.py runserver`

Accessing the System:

Once the backend server is running, you can access the system by opening your web browser and entering the following URL:

	`http://localhost:8000`

You can also access the admin interface from this URL:

	`http://localhost:8000/admin`
