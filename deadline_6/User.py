import mysql.connector
# import googlemaps
import random

import getpass

def display_menu():
    print("\nAV Cabs")
    print("1. Sign Up")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")
    return choice

def sign_up(users):
    print("\nSign Up")
    firstname = input("First Name: ")
    mid_name = input("Middle Name: ")
    lastname = input("Last Name: ")

    if username in users:
        print("Username already exists. Please try a different one.")
        return

    password = getpass.getpass("Enter a password: ")
    users[username] = password
    print("Registration successful!")

def login(users):
    print("\nLogin")
    username = input("Enter your username: ")

    if username not in users:
        print("Username not found. Please sign up.")
        return

    password = getpass.getpass("Enter your password: ")

    if users[username] == password:
        print("Login successful!")
        book_cab()
    else:
        print("Incorrect password. Please try again.")





