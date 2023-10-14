from mysql.connector import connect, Error


def show_menu() -> None: print(f"\n1 - execute a show query\n2 - execute an update query\n3 - exit\n")


try:
    with connect(
            host="localhost",
            database=input("database: "),  # sakila
            user=input("User name: "),  # root
            password=input("Password: ")
    ) as connection:
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            with connection.cursor() as cursor:
                cursor.execute("SELECT DATABASE();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                while True:
                    show_menu()
                    choice = input("User input: ")
                    try:
                        if choice in ("1", "2"):
                            query_lines = []
                            print("Enter query: ")
                            while True:
                                query_input = input()
                                if query_input != "":
                                    query_lines.append(query_input)
                                else:
                                    final_query = ' '.join(query_lines)
                                    cursor.execute(final_query)
                                    match choice:
                                        case "1":
                                            for item in cursor:
                                                print(*item)
                                            break
                                        case "2":
                                            connection.commit()
                                            break
                        elif choice == "3":
                            break
                        else:
                            print("Invalid input")
                    except Error as e:
                        print("Error while executing a query", e)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    print("MySQL connection is closed")

# TEST QUERIES

# 1 -----------------------------------
# UPDATE QUERY
# use sakila (if not already using this data base)

# SHOW QUERY
# SELECT film_id, title, rating, 'children'
# FROM film
# WHERE rating in ("G","PG","PG-13")
# UNION
# SELECT film_id, title, rating, 'adults'
# FROM film
# WHERE rating in ("R","NC-17")
# ORDER BY film_id
# -------------------------------------

# 2 -----------------------------------
# UPDATE QUERY
# use sakila (if not already using this data base)

# SHOW QUERY
# SELECT a.first_name, fa.film_id, f.title
# FROM actor a
# LEFT JOIN film_actor fa
# USING (actor_id)
# LEFT JOIN film f
# USING (film_id)
# -------------------------------------

# 3 -----------------------------------
# UPDATE QUERY
# USE sakila (if not already using this data base)
# UPDATE actor
# SET first_name = "Joe2"
# WHERE actor_id = 2
# -------------------------------------
