import subprocess


def search_logs(username):
    # Path to the log file
    log_file_path = '/var/log/auth.log'

    # Construct the grep command to search for the username
    grep_command = f'grep {username} {log_file_path}'

    try:
        # Execute the grep command
        result = subprocess.run(grep_command, shell=True, text=True, capture_output=True)

        # Check if the search was successful
        if result.returncode == 0:
            # Print the found log entries
            print(f"Log entries for user '{username}':\n{result.stdout}")
        else:
            # Print an error message if no entries are found
            print(f"No log entries found for user '{username}'.")
    except Exception as e:
        # Print any error that occurs during the subprocess execution
        print(f"An error occurred: {e}")


# entry into main app
username = 'natato'
search_logs({username})
