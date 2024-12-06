#!/usr/bin/python3
"""
    Print statistics in the required format.
    :param file_size: Total file size computed so far.
    :param status_codes: Dictionary of status codes and their counts.
    """
import sys


def print_stats(file_size, status_codes):
    """
    Print statistics in the required format.
    :param file_size: Total file size computed so far.
    :param status_codes: Dictionary of status codes and their counts.
    """
    print(f"File size: {file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    # Initialize variables
    file_size = 0
    status_codes = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0}
    line_count = 0

    # Process input from stdin line by line
    try:
        for line in sys.stdin:
            # Parse the line
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip invalid lines

            try:
                # Extract status code and file size
                status_code = int(parts[5])
                size = int(parts[6])
            except ValueError:
                continue
            # If the status code or size is not valid, skip this line

            # Validate the status code
            if status_code not in status_codes:
                continue  # Skip lines with invalid status codes

            # Update counters
            file_size += size
            status_codes[status_code] += 1
            line_count += 1

            # Print stats after every 10 lines
            if line_count % 10 == 0:
                print_stats(file_size, status_codes)

    except KeyboardInterrupt:
        # Print stats if the program is interrupted by the user
        print_stats(file_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
