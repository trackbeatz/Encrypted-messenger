# 🛡️ TRACK: SECURE MESSENGER
**Asymmetric RSA Encryption for Termux**

`TRACK` is a secure communication tool built for the CODEX environment. It uses RSA-2048 encryption to ensure that only the holder of a specific Private Key can read a message encrypted with its corresponding Public Key.

---

## 📥 QUICK START (Termux)

1. **Install Python & Cryptography:**
   ```bash
   pkg update && pkg upgrade
   pkg install python
   pip install cryptography
2  Navigate to Directory:
cd storage/shared/program/cryptograph
3. Run the system

   python crypt.py
   
## 🚀 OPERATION GUIDE


​1️⃣ Identity Setup
​Run the script and select Option 1.
​Results: Two files are created:
​my_private_key.pem: Your digital fingerprint. NEVER SHARE.
​my_public_key.pem: Your "mailbox." SHARE THIS with anyone who wants to message you.
​2️⃣ Sending a Secret
​Obtain your friend's my_public_key.pem.
​Place it in your folder (rename it to friend.pem).
​Select Option 2 in the script.
​Input the path: friend.pem.
​Copy the outputted ENCRYPTED DATA and send it via any chat app.
​3️⃣ Decrypting a Secret
​Copy the scrambled text your friend sent you.
​Select Option 3 in the script.
​Paste the string and press Enter.
​The system reveals the message and the exact time it was created.


​🛡️ SECURITY PROTOCOLS
​Asymmetric Logic: Data locked with a Public Key cannot be unlocked by a Public Key. Only the Private Key works.
​Tamper Proof: If even one character of the encrypted string is changed, decryption will fail.
​Terminal Colors: * MAGENTA: System Branding
​CYAN: Status Info
​GREEN: Success/Verified
​RED: Security Alert/Error
​Secure Logistics Tracker - Codex Edition

