#  Encrypted Chat

A simple Python local chat demo where messages are encrypted before sending and decrypted when read.

## Features
- Two participants (Alice & Bob)
- Messages are encrypted using `cryptography`
- Local chat log with decrypted view option

## Setup
1. Clone the repository
   ```bash
   git clone https://github.com/YOUR-USERNAME/encrypted-chat.git
   cd encrypted-chat
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run the chat

bash
Copy code
python chat.py
Security Notes
This is a local simulation, not for real networking.

Encryption key is stored in chat.key. Keep it safe.

yaml
Copy code

---

###  How it works
- When **Alice or Bob sends a message**, it’s encrypted and stored in memory.  
- When viewing the **chat log**, messages are decrypted and displayed.  
- The key is saved in `chat.key` so messages can be decrypted later.  

---

If you want, I can also create the **GitHub-ready version** for this project, with:  
- `.github/workflows/ci.yml` (for lint/tests)  
- LICENSE (MIT)  
- `.env.template` if you want to make the key configurable  

This way, you can **publish it directly** like your other projects.  

Do you want me to do that?
