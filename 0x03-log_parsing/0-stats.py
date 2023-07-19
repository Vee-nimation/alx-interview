#!/usr/bin/python3
# Initialize variables to store metrics
total_file_size = 0
status_code_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def print_statistics():
    print("Total file size: File size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        count = status_code_count[status_code]
        if count > 0:
            print(f"{status_code}: {count}")

def process_line(line):
    global total_file_size
    try:
        parts = line.split()
        ip_address, _, _, _, _, _, _, _, status_code_str, file_size_str = parts
        status_code = int(status_code_str)
        file_size = int(file_size_str)

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_code_count:
            status_code_count[status_code] += 1

    except (ValueError, IndexError):
        # Skip the line if the format is not as expected
        pass

def signal_handler(signal, frame):
    # Print statistics and exit on keyboard interruption (CTRL + C)
    print_statistics()
    sys.exit(0)

if __name__ == "__main__":
    # Register the signal handler for CTRL + C
    signal.signal(signal.SIGINT, signal_handler)

    try:
        line_count = 0
        while True:
            line = sys.stdin.readline().strip()
            if not line:
                # End of input
                break

            process_line(line)
            line_count += 1

            if line_count % 10 == 0:
                print_statistics()

    except KeyboardInterrupt:
        # CTRL + C is pressed
        pass

    # Print final statistics
    print_statistics()
