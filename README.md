# 📧 Serverless Email API  

A REST API built using the **Serverless Framework** that sends emails based on user input.  
The API accepts **receiver_email**, **subject**, and **body_text** and sends an email accordingly with proper error handling and HTTP response codes.  

---

## 🚀 Features  

- 🌐 REST API powered by Serverless Framework  
- 📩 Send emails dynamically using inputs  
- ✅ Error handling with appropriate HTTP status codes  
- ⚡ Supports **serverless-offline** for local testing  
- ☁️ Integrates with **AWS SES** for email delivery  
- 🖥️ Can be tested with **Postman**  

---

## 🛠️ Tech Stack  

- **Backend**: Python  
- **Database / Storage**: N/A (stateless API)  
- **Email Service**: AWS SES (Simple Email Service)  
- **Language**: Python  
- **Testing**: Postman / Curl  

---

## Project Demo: Registration System  

[![Watch the video](https://img.shields.io/badge/Watch-Video-blue)](https://drive.google.com/file/d/1Vjg19PNcNnV4vFkyHlnq8C64OMldGOjG/view?usp=sharing)


## 📦 Installation & Setup  

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/serverless-email-api.git
   cd serverless-email-api

2. **Create Virtual Environment & Activate**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # Mac/Linux

3. **Install Dependencies**
   ```bash
     pip install -r requirements.txt

4. **Configure AWS SES credentials**  
   - Make sure your AWS Access Key and Secret Key are set up in `~/.aws/credentials`  
   - Verify sender and receiver emails in AWS SES sandbox (or move to production)
  
5. **Start Serverless Offline**  
   Run the following command to start the server locally:  

   ```bash
   serverless offline

## 📬 API Usage  

### Endpoint  
### Request Body (JSON)  
```json
{
  "receiver_email": "example@email.com",
  "subject": "Hello from Serverless",
  "body_text": "This is a test email using the Serverless Framework!"
}


  
   




   

   









