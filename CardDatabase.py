from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode


def main():
    try:
        myDB = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='CardManagement')
        cursor = myDB.cursor()

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    else:
        print("")

    while True:
        print("")
        print("What do you want to do?")
        option = int(input("Choose your option - 0: print members 1: new member 2: print cards 3: new card "))

        if option == 0:
            cursor.execute("SELECT * FROM member")
            result = cursor.fetchall()
            print("")
            print(result)
            print("")

        elif option == 1:
            ID = str(input("What is the ID? : "))
            PW = str(input("What is the password? : "))
            name = str(input("What is the name? : "))
            BD = str(input("What is the Birth Date?(format -> 19801010) : "))
            PN = str(input("What is the Phone Number? (format -> 01011112222) : "))

            cursor.execute("INSERT INTO member VALUES(\"" + ID + "\", \"" + PW + "\", \"" + name + "\", \"" + BD + "\", \"" + PN + "\")")
            myDB.commit()
            print("Insertion Done!")

        elif option == 2:
            cursor.execute("SELECT * FROM card")
            result = cursor.fetchall()
            print("")
            print(result)
            print("")

        elif option == 3:
            CN = str(input("What is the Card Number? : "))
            RD = str(input("What is the Registration Date? (format -> 19801010) : "))
            account = str(input("What is the connected account? : "))
            point = str(input("How much is the initial point? : "))
            valid = str(input("Is it valid? : "))

            cursor.execute("INSERT INTO card VALUES(\"" + CN + "\", \"" + RD + "\", \"" + account + "\", \"" + point + "\", \"" + valid + "\")")
            myDB.commit()
            print("Insertion Done!")

        else:
            print("I don't understand... ")


########################################################################


if __name__ == '__main__':
    main()
