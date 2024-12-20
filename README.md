# Finwise: Financial AI Chatbot

## Project Overview

**Finwise** is an intelligent financial chatbot designed to provide users with financial advice and assistance. Utilizing generative AI technologies, Finwise can engage users in conversation, prompting them with relevant advice tailored to their financial inquiries.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Generative AI Integration:** Provides intelligent financial advice based on user input.
- **User-Friendly Interface:** Engages users through a conversational interface.
- **Customizable Responses:** Adapts responses based on user queries and context.

## Tech Stack

- **Programming Language:** Python
- **Framework:** Flask
- **Template Engine:** Jinja2
- **Frontend:** HTML, CSS
- **AI Technology:** Generative AI SDK
- **Cloud Platform:** GCP Vertex AI

## Demo
[View PDF](https://github.com/bhpham/finwise-chatbot/blob/main/demo.pdf)


## Installation

To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/finwise-chatbot.git
   cd finwise-chatbot

2. Install dependencies: Make sure you have the required Python packages installed. You can create a virtual environment if desired.
   ```bash
   pip install -r requirements.txt

4. Configure API Keys:
Create API keys in GCP Vertex AI or Service Account keys.
Add your key to the .env file in the root directory. 
5. Run the applications on localhost:
   ```bash
   python3 app.py

Usage
Open your browser and navigate to http://localhost:5000 to access the chatbot interface.
Interact with the chatbot by asking questions related to financial advice.

Deployment
Finwise will soon be deployed on RapidAPI for broader access and outsourcing usage. Stay tuned for updates on deployment and access details.

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add your feature').
Push to the branch (git push origin feature/YourFeature).
Create a pull request.
License
This project is licensed under the MIT License.


### Notes to run application on local machine:
1. Create API keys Vertex AI or Service Account keys in Google Cloud Platform console.
2. Add key to .env file under the project environment file.
