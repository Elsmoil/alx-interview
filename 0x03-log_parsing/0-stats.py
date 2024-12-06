#!/usr/bin/python3
import sys
    """
    Print statistics in the required format.
    :param file_size: Total file size computed so far.
    :param status_codes: Dictionary of status codes and their counts.
    """


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
            # Check if line matches the expected format
            parts = line.split()
            if len(parts) < 7:
                continue  # Skip lines that don't have enough parts

            # Extract status code and file size from the line
            try:
                status_code = int(parts[5])  # Status code is at index 5
                size = int(parts[6])  # File size is at index 6
            except ValueError:
                continue  # Skip lines where the status code or size is invalid

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

        # After finishing reading all lines, print final stats
        if line_count > 0:
            print_stats(file_size, status_codes)
        else:
            print("File size: 0")  # Handle empty file case

    except KeyboardInterrupt:
        # Handle keyboard interrupt (CTRL + C) and print stats
        if line_count > 0:
            print_stats(file_size, status_codes)
        else:
            print("File size: 0")
        sys.exit(0)


if __name__ == "__main__":
    main()
