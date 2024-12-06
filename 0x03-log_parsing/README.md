Usage:

    Save the script as 0-stats.py.
    You can test it with the generator script (0-generator.py) provided in the repo, or you can pipe log data into it.

Example usage:

./0-generator.py | ./0-stats.py

This will generate a continuous stream of log lines, and 0-stats.py will compute and print the statistics every 10 lines or when interrupted.
Edge Cases:

    Invalid format: Lines that don’t match the expected format will be skipped.
    Invalid status code or file size: If the status code or file size is missing or not a valid integer, the line is skipped.
    Keyboard interruption: The script handles CTRL + C gracefully and prints the accumulated statistics before exiting.

This solution handles the problem requirements efficiently and ensures the correct output in a variety of situations.
