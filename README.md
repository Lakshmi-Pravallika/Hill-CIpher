# Hill-CIpher
Encryption:
In order to encrypt a message using the Hill cipher, the sender and receiver must first agree upon a key matrix A of size n x n. Amust be invertible mod 26. The plaintext will then be enciphered in blocks of size n. In the following example A is a 2 x 2 matrix and the message will be enciphered in blocks of 2 characters.  
Key Matrix: A =[3 25
                24 17]
Message: MISSISSIPPI
The first block MI corresponds to the matrix  . The sender will then calculate:
A[12 8]  =[2 8]  (mod 26)
The first two letters of the ciphertext correspond to 2,8 and are therefore CI. This step is repeated for the entire plaintext. If there are not enough letters to form blocks of 2, pad the message with some letter, say Z.
The message:	
    MI SS IS SI PP IK
will be enciphered as:
    CI KK GE UW ER OY
Notice that the repeated digraphs IS, SS and repeated letters S and P in the plaintext are masked using the Hill cipher.

Decryption:
To decipher a message, first calculate the inverse of the key A.
Then multiply the inverse of the key by each pair of ciphertext letters (mod 26) to recover the original text.
   Key Matrix: A = [3 17
                    8 25]
Encrypted Message: CIKKGEUWEROY
The receiver will calculate:
A -1 [2 8]=[12 8] (mod 26)
to decrypt the message. The first two letters are 12, 8 which correspond to M and I. The receiver will repeat this step for every pair of letters in the ciphertext to recover the original message MISSISSIPPIK.



