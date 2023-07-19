#!/usr/bin/python3

import sys
from collections import defaultdict

def print_statistics(file_sizes, status_counts):
    total_size = sum(file_sizes)
    print(f"Total file size: File size: {total_size}")
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def process_input():
    file_sizes = []
    status_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1

            # Parse the line in the given format
            parts = line.split()
            if len(parts) != 7 or not parts[3].isdigit():
                continue

            _, _, _, _, status_code, file_size, _ = parts

            # Check if status_code is valid and add it to status_counts
            try:
                status_code = int(status_code)
                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_counts[status_code] += 1
            except ValueError:
                pass

            # Add the file size to file_sizes
            try:
                file_size = int(file_size)
                file_sizes.append(file_size)
            except ValueError:
                pass

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(file_sizes, status_counts)

    except KeyboardInterrupt:
        pass

    # Print final statistics
    print_statistics(file_sizes, status_counts)

if __name__ == "__main__":
    process_input()
