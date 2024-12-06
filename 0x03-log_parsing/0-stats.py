#!/usr/bin/python3

"""
      Prints the accumulated statistics: total file size and
      count of each status code.

      Args:
          file_size (int): The total file size accumulated so far.
          status_codes (dict): A dictionary of status codes and their
                               respective counts.

      Prints:
          File size: The total file size computed so far.
          <status code>:
          <count> for each status code with a count greater than 0.
          The status codes are printed in ascending order.
"""

import sys
import re


def initialize_log():
    # Define the status codes as list
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    log = {
        "file_size": 0,
        # Initialize counts for each status code
        "code_list": {str(code): 0 for code in status_codes}
    }
    return log


def parse_line(line, regex, log):
    """
    Parses a line using regex to extract status code and file size
    and updates the log accordingly.

    Args:
        line (str): The log line to parse.
        regex (regex): The compiled regex pattern for extracting info.
        log (dict): The accumulated log data.

    Returns:
        dict: Updated log.
    """
    match = regex.fullmatch(line)
    if match:
        status_code, file_size = match.group(1, 2)
        log["file_size"] += int(file_size)  # Accumulate total file size
        if status_code.isdecimal():
            # Count occurrences of status code
            log["code_list"][status_code] += 1
    return log


def print_codes(log):
    """
    Prints the accumulated file size and status code counts.

    Args:
        log (dict): The accumulated log data.
    """
    print(f"File size: {log['file_size']}")
    # Sort the codes in ascending order
    sorted_codes = sorted(log["code_list"].keys())
    for code in sorted_codes:
        if log["code_list"][code] > 0:
            print(f"{code}: {log['code_list'][code]}")


def main():
    # Regex pattern for matching log lines
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \['
        r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})\] '
        r'"GET /projects/\d+ HTTP/1.1" (\d{3}) (\d+)')

    # Initialize the log data
    log = initialize_log()
    line_count = 0

    try:
        # Read log lines from stdin
        for line in sys.stdin:
            line = line.strip()  # Clean up the line
            line_count += 1

            # Parse the line and update the log
            log = parse_line(line, regex, log)

            # Print stats every 10 lines
            if line_count % 10 == 0:
                print_codes(log)

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nProcess interrupted by user.")
        print_codes(log)


if __name__ == "__main__":
    main()
