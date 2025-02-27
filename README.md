# Cryptography-CP-ABE
## Introduction: ENCRYPTION, ACCESS CONTROL AND QUERY ON CLOUD DATABASE IN REAL ESTATE TRANSACTIONS 

Ciphertext-Policy Attribute-Based Encryption (CP-ABE) is a sophisticated encryption method that enables data access based on user attributes. The ciphertext is embedded with a special policy, allowing only users with attributes that match the policy to decrypt it. This approach enhances flexibility and fine-grained access control, particularly in environments like cloud storage where data might need to be shared selectively.

This project is applied in the real estate field, utilizing two CP-ABE schemas, SP21 and BSW07, for policy encryption. The relevant external parties include customers, government employees, banks, and company employees. Currently, the project has achieved confidentiality in terms of security goals but lacks authentication and authorization mechanisms.
### Problem Context:
* Real estate companies need to store and manage documents related to transactions, contracts, and legal records.
* Data is stored on the cloud and must be securely accessed by multiple parties (company employees, banks, public administration agencies, etc.).
* The challenge is how to enforce access control so that only authorized individuals can read or modify the data.
![Image](https://github.com/user-attachments/assets/919df18e-8efe-49fe-ba64-7516fce4c978)

### Stakeholders and Threats
* Data Owners: Individuals or entities that own and manage the data.
* Data Users: Authorized individuals who have access to the data (employees, banks, public administration agencies).
* Cloud Storage: The platform where data is stored, acting only as an intermediary without permission to read the content.
* Threats:
  - Semi-trusted third party: The cloud provider may have access to the data.
  - Impersonators: Attackers who disguise themselves as authorized users to gain unauthorized access to the data.

 ![Image](https://github.com/user-attachments/assets/c3c3d8f8-2ee5-411d-98a2-db105c5deccd)

 ### Security Solutions
* Authentication & Authorization: Ensures that only authorized users can access the system.
* Data Confidentiality:
  * AES Symmetric Encryption: Ensures that data stored on the cloud cannot be read by third parties.
  * CP-ABE (Ciphertext Policy Attribute-Based Encryption): Allows only users with matching attributes to decrypt the data.
  * Diffie-Hellman Key Exchange: Dynamically generates secret keys to protect query information and data.
 
![Image](https://github.com/user-attachments/assets/91724e99-09f0-45e6-936a-92083907d854)
![Image](https://github.com/user-attachments/assets/7da71bfa-1712-490c-81ba-15241bdffdc4)

### Implementation and Evaluation
* The system is tested in a Linux environment with simulated nodes (bank server, users with different access rights).
* Testing steps include key generation, data encryption, cloud storage, query control, and decryption based on policies.
* The system effectively enforces access control, but it lacks server-side authentication to ensure users do not mistakenly access the wrong server.
