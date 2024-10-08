from db_layer import connect_to_database, insert_user, fetch_users

def add_user_logic(name, age):
    try:
        age = int(age)
    except ValueError:
        return False, "Age must be a number."

    connection = connect_to_database()
    if not connection:
        return False, "Failed to connect to the database."

    success, message = insert_user(connection, name, age)
    connection.close()

    return success, message

def get_users_logic():
    connection = connect_to_database()
    if not connection:
        return []

    users = fetch_users(connection)
    connection.close()

    return users
