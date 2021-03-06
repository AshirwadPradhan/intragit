#Generate CA's private and public key
# This enables us to become the CA

from pki_util import generate_private_key, generate_public_key
import os

if __name__ == "__main__":
    certpath = os.path.join(os.getcwd(),'src','')
    private_key = generate_private_key(certpath+'ca-private-key.pem', 'this')

    generate_public_key(private_key=private_key,
                        filename=certpath+'ca-public-key.pem',
                        country='IN',
                        state='Rajasthan',
                        locality='Pilani',
                        org='BITS CSIS Department',
                        hostname='bits-pilani-CA.ac.in')