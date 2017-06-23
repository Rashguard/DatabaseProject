from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode


def main():
    try:
        myDB = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='CardManagement')

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    else:
        myDB.close()

    cursor = myDB.cursor()

    while True:
        print("What do you want to do?")
        option = int(input("Choose your option - 0: print members 1: new member 2: new card "))

        if option == 0:
            cursor.execute("SELECT * FROM member")

        elif option == 1:
            ID = input("What is the ID? : ")
            PW = input("What is the password? : ")
            name = input("What is the name? : ")
            BD = input("What is the Birth Date?(format -> 19801010) : ")
            PN = input("What is the Phone Number? (format -> 01011112222) : ")

            cursor.execute("INSERT INTO member VALUES(" + ID + ", " + PW + ", " + name + ", " + BD + ", " + PN + ")")

        elif option == 2:
            cursor.execute("")

        else:
            print("I don't understand... ")


########################################################################


if __name__ == '__main__':
    main()
