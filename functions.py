def read_from_file():
    """Read from tasks.txt and return the value in from of a dict."""
    s = {}
    filename = '/home/ishaan/Documents/Ishaan\'s-Coding/coding-in-python/tasks.txt'
    with open(filename) as file:
        for line in file:
            f = line.rstrip('\n')
            d = line.split(' : ')
            s[d[0]] = d[1]
    return s

def append_to_file():
    filename = '/home/ishaan/Documents/Ishaan\'s-Coding/coding-in-python/tasks.txt'
    with open(filename, 'a') as f:
        f.write(f"{task_entry.get()} : {date_entry.get()}")
    showinfo(title='Tast sucessful', message='Task Sueccful!!')