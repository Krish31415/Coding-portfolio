def main():
    import keyboard

    # Record keys
    recorded = keyboard.record(until="esc")

    # Make a new list of names of keys
    record = [a.name for a in recorded if a.event_type == "down"]
    record.pop()

    # Replace backspaces
    while 'backspace' in record:
        record.pop(record.index('backspace') - 1)
        record.remove('backspace')

    # Replace word space with actual space
    record = [" " if a == "space" else a for a in record]
    # Replace enter with newline
    record = ["\n" if a == "enter" else a for a in record]
    # Remove special keys
    record = ["" if len(a) != 1 else a for a in record]
    print("".join(record))

    # Write to file
    log = open('log.txt', 'a')
    log.write(''.join(record) + '\n')
    log.close()


if __name__ == '__main__':
    main()