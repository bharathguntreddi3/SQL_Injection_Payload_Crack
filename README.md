# <h1 align = "center">SQL _Injection And Password cracker</h1>

<p align = "center"><img src = "https://user-images.githubusercontent.com/95229816/161307250-e4f4d8ce-1079-4e20-adbf-bb414ee100b0.gif", height="400px", width="100px"></p>

#### This Repo contains a detailed usage of subprocess, hashlib modules.I have used the subprocess module to process my 'NETSH WLAN SHOW PROFILES' command and output your current working PC wifi connectivities and thier passwords.This Repo consists a msg 5 hash Alogrithm to generate a 'md5 hash' and the 'SHA Algorithm' to produce the corresponding hashes.A password generator using random library and shows the working of SQL Injection and prevention. 

# <h1 align="center">SQL Injection</p>

## What is SQL Injection?
SQL injection, also known as SQLI, is a common attack vector that uses malicious SQL code for backend database manipulation to access information that was not intended to be displayed. This information may include any number of items, including sensitive company data, user lists or private customer details.It occurs when a attacker infuses malicious code into SQl statement using, via web page input.

SQL is a standardized language used to access and manipulate databases to build customizable data views for each user.

SQL injection usually occurs when you ask a user for input, like their username/userid, and instead of a name/id, the user gives you an SQL statement that you will unknowingly run on your database.

Example:

```sql
SELECT ItemName, ItemDescription
FROM Item
WHERE ItemNumber = ItemNumber
```

From this, the web application builds a string query that is sent to the database as a single SQL statement:

```sql
sql_query= "
SELECT ItemName, ItemDescription
FROM Item
WHERE ItemNumber = " & Request.QueryString("ItemID")
```

```sql
SELECT * FROM Users WHERE UserId = 105 OR 1=1;
-- Above query is valid and returns data from users, since 'OR 1=1' is always true
```

<p align="center"><img src="https://user-images.githubusercontent.com/95229816/161307971-6b64d880-8e8c-4a6a-8a08-11f4d6003bcc.jpg" align="center"></p>

# Demo:
#### I have created a form using html and created a database using php where the data is stored.
The attacker can run the above mentioned queries to exploit the data in the database

### Below shows how to build parameterized queries in PHP : 
```php
 <?php

    $username = $_POST['username'];
    $password = $_POST['password'];

    $conn = new mysqli('localhost', 'root', '', 'sql_injection');

    if($conn->connect_error){
        die('connection Failed : ' .$conn->connect_error);
    }else{
        $stmt = $conn->prepare("insert into sql_injection(username, password)");

        $stmt->bind_param("ss",$username, $password);
        $stmt->execute();
        $stmt->close();
        $conn->close();
    }
?>
```

If you a Database Administrator or a database enthusiast like me then you can use python or R to connect to database rather than php.

```python
# pip install cx_oracle 
import cx_Oracle    # for oracle any verison
# pip install pyodbc
import pyodbc       # for sqlserver
# pip install mysql.connector
import mysql.connector      # for MySQL
# pip install psycopg2
import psycopg2      # for postgre SQl

# you can connect to your database using these imports and creating a 'cursor' to access output queries
```
<p align="center"><img src="https://user-images.githubusercontent.com/95229816/161308314-5f41c6ca-ecc0-4c00-8f1c-0d13406fcb31.jpg", width="70%", height="70%"></p>

# Types:

### <h3><u>1.In-band SQLi :</u></h3>  The attacker uses the same channel of communication to launch their attacks and to gather their results. In-band SQLi’s simplicity and efficiency make it one of the most common types of SQLi attack

### <h3><u>2.Inferential (Blind) SQLi :</u></h3>  The attacker sends data payloads to the server and observes the response and behavior of the server to learn more about its structure. This method is called blind SQLi because the data is not transferred from the website database to the attacker, thus the attacker cannot see information about the attack in-band.

# Prevention : 

### <h3><u>1.Update your database management software :</u></h3>  You can protect yourself by just patching and updating your database management software.

### <h3><u>2.Enforce the principle of least privilege (PoLP) :</u></h3>  PoLP means each account only has enough access to do its job and nothing more. A web account that only needs read access to a given database shouldn't have the ability to write, edit or change data in any way.

### <h3><u>3.Use prepared statements or stored procedures :</u></h3>  As opposed to dynamic SQL, prepared statements limit variables on incoming SQL commands.

### <h3><u>4.OWASP :</u></h3>  The Open Web Application Security Project, OWASP for short, is the leading authority on web applications and they have lots of additional reading on how to prevent SQL injections.

<h3>For any additional information do check <a href="https://owasp.org/www-community/attacks/SQL_Injection">SQL Injection</a></h3>

<p>-------------------------------------------------------------------------------------------------------------------------------------------------------------</p>

                                   __________________            ___________________  
                                 /                             /                     \            |                  
                                |                             |                       |           |    
                                |                             |                       |           |     
                                |                             |                       |           |
                                |                             |                       |           |
                                \                             |                       |           |
                                 \________________            |                       |           |
                                                   \          |                       |           |
                                                    |         |                 \     |           |
                                                    |         |                  \    |           |
                                                    |         |                   \   |           |
                                                    |         |                    \  |           |
                                                   /           \ ___________________\/            |________________________   
                               __________________ /                                  \                       
                                                                                      \
                                                                                       \
                                                                                       ` \     

<p>-------------------------------------------------------------------------------------------------------------------------------------------------------------</p>

# <h1 align="center">Password Cracker And Hash Algorithms</h1>

### <h3><u>Hashing :</u></h3>  Hashing is a technique or process of mapping keys, values into the hash table by using a hash function. It is done for faster access to elements. The efficiency of mapping depends on the efficiency of the hash function used.

hashlib implements a common interface to many different secure hash and message digest algorithms. Included are the FIPS secure hash algorithms SHA1, SHA224, SHA256, SHA384, and SHA512 (defined in FIPS 180-2) as well as RSA’s MD5 algorithm (defined in internet RFC 1321). 

hashlib - The hashlib module defines an API for accessing different cryptographic hashing algorithms.

HASH Algorithms:

1.md5

2.sha1

3.sha224

4.sha256

5.sha384

6.sha512

7.sha3_224, sha3_256, sha3_384, sha3_512 

# [md5 Algorithm](https://docs.python.org/3/library/hashlib.html)

MD5 (Message Digest Method 5) is a cryptographic hash algorithm used to generate a 128-bit digest from a string of any length. It represents the digests as 32 digit hexadecimal numbers.

<p align="center"><img src="https://user-images.githubusercontent.com/95229816/161313683-ad81d452-8a2e-4f94-8ebd-b76d31ef220c.png", width="70%", height="70%"><p>


### <h3><u>Hash Function :</u></h3>  A function that converts a given big phone number to a small practical integer value. The mapped integer value is used as an index in the hash table. In simple terms, a hash function maps a big number or string to a small integer that can be used as the index in the hash table. 

NOTE : A good hash function should a Efficiently computable and Should uniformly distribute the keys (Each table position equally likely for each key)

Generating md5 hash:

Requirement:
```python
import hashlib
```

```python
import hashlib

user_pass = input("Enter any Character or string or number : ")
enco = hashlib.md5(user_pass.encode())     # encode the input

res_hash = enco.hexdigest()          # convert to hexa decimal format
print("Your Hash Value : "+ str(hash(user_pass)))
print("Your encoded Hash code : ",res_hash)
```

# [SHA Algorithm](https://docs.python.org/3/library/hashlib.html)

SHA 256 is a part of the SHA 2 family of algorithms, where SHA stands for Secure Hash Algorithm. SHA-256 Algorithm is currently used most for secure hashing, since of 256 in the name stands for the final hash digest value, i.e. irrespective of the size of plaintext/cleartext, the hash value will always be 256 bits.

<p align="center"><img src="https://user-images.githubusercontent.com/95229816/161316793-f368bb22-2217-41ff-9aa8-85c4f91012e1.jpg", width="70%", height="70%"></p>

### <h1>Characteristics : </h1>

### <h3><u>Message Length :</u></h3>  The length of the cleartext should be less than 264 bits. The size needs to be in the comparison area to keep the digest as random as possible.

### <h3><u>Digest Length :</u></h3>   The length of the hash digest should be 256 bits in SHA 256 algorithm, 512 bits in SHA-512, and so on. Bigger digests usually suggest significantly more calculations at the cost of speed and space.

### <h3><u>Irreversible :</u></h3>    By design, all hash functions such as the SHA 256 are irreversible. You should neither get a plaintext when you have the digest beforehand nor should the digest provide its original value when you pass it through the hash function again.

<p align="center"><img src="https://user-images.githubusercontent.com/95229816/161316816-a2c47574-2835-4415-8890-3f19e05d3110.jpg", width="70%", height="70%"></p>

```python
import hashlib
user_pass = input("Enter Any character or String or Number :")
sha1 = hashlib.sha1(user_pass.encode())
sha224 = hashlib.sha224(user_pass.encode())
sha256 = hashlib.sha256(user_pass.encode())
sha384 = hashlib.sha384(user_pass.encode())
sha512 = hashlib.sha512(user_pass.encode()
# digest the function
print("SHA1 hash Code :", sha1.hexdigest())
print("SHA224 hash Code :", sha224.hexdigest())
print("SHA256 hash Code :", sha256.hexdigest())
print("SHA384 hash Code :", sha384.hexdigest())
print("SHA512 hash Code :", sha512.hexdigest())
```

# Applications :

<p align="center"><img src="https://user-images.githubusercontent.com/95229816/161316883-a04b4568-e31c-424d-a9f0-a854857c9204.jpg", width="70%", height="70%"></p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/95229816/161365323-5c226215-2e5f-4607-bd9e-63cc6c399dc7.png", width="30%", height="30%">
  <img src="https://user-images.githubusercontent.com/95229816/161365328-8e40efee-5fc7-41af-bb7b-c45cc85415fb.png", width="30%", height="30%">
</p>

My Database is Starving !!!


<h3>If any necessary commits are required to increase the elegance of this repo! i'm always open for a PR.</h3>

### <h2>With this signing off..!!,BHARATH GUNTREDDI ..🤞</h2>

