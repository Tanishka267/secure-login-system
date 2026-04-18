A beginner-friendly backend security project demonstrating authentication and basic cybersecurity practices.
#  Secure Login System (Flask)
A simple and secure user authentication system built using Flask. This project demonstrates basic security practices like password hashing, strength validation, and login attempt limiting.

##  Features

- User Registration & Login system
- Password hashing using SHA-256
- Password strength validation (Weak / Medium / Strong)
- Login attempt limiting (account lock after 3 failed attempts)
- Backend web application built using Flask framework
## Tech Stack

- Python
- Flask
- Regular Expressions (Regex)
- Hashlib (for password encryption)

##  Project Structure
secure-login-system/
│── app.py
│── requirements.txt
│── README.md

##  How to Run the Project

1. Install dependencies:
2. Run the app:
3. Open in browser:
   http://127.0.0.1:5000/

##  Security Features Implemented

- Passwords are hashed using SHA-256 before storing
- Password strength is checked using regex rules
- Account gets temporarily locked after multiple failed login attempts


## Screenshots

<img width="515" height="322" alt="image" src="https://github.com/user-attachments/assets/6bf4eeb9-11dc-4b16-9ce6-b98215ef6947" />
<img width="419" height="219" alt="image" src="https://github.com/user-attachments/assets/4b2f780f-09f8-4f94-af09-d5f9f8f75bdb" />
<img width="284" height="86" alt="image" src="https://github.com/user-attachments/assets/cdcc9095-78cc-413a-831d-22d9a8378ecf" />
<img width="505" height="269" alt="image" src="https://github.com/user-attachments/assets/d1cd9c8c-5f9d-4534-8206-f4c0407fe9fd" />
<img width="484" height="244" alt="image" src="https://github.com/user-attachments/assets/7c5db93a-3aae-49c5-afd3-7f71098bfc00" />

## Future Improvements

-Add database integration (SQLite / MySQL)
-Implement user sessions and logout functionality
-Build a frontend UI (HTML/CSS or React)
-Deploy the application (Render / AWS / Heroku)
-Replace SHA-256 with stronger hashing (e.g., bcrypt)

Author

Tanishka Vatsa
https://github.com/Tanishka267

