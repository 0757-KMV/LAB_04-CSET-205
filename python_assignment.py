class Process:
    def __init__(self, p_id, name, start_time, priority):
        self.p_id = p_id
        self.name = name
        self.start_time = start_time
        self.priority = priority
    
    def __str__(self):
        return f"Process {self.p_id}: {self.name} (Start Time: {self.start_time} ms, Priority: {self.priority})"

def sort_processes(processes, key):
    if key == 1:
        return sorted(processes, key=lambda p: p.p_id)
    elif key == 2:
        return sorted(processes, key=lambda p: p.start_time)
    elif key == 3:
        return sorted(processes, key=lambda p: (p.priority, p.start_time))

def main():
    processes = [
        Process("P1", "VSCode", 100, "MID"),
        Process("P23", "Eclipse", 234, "MID"),
        Process("P93", "Chrome", 189, "High"),
        Process("P42", "JDK", 9, "High"),
        Process("P9", "CMD", 7, "High"),
        Process("P87", "NotePad", 23, "Low")
    ]
    
    while True:
        print("\nMenu:")
        print("1. Sort by Process ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Quit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 4:
            break
        
        if choice < 1 or choice > 3:
            print("Invalid choice. Please select a valid option.")
            continue
        
        sorted_processes = sort_processes(processes, choice)
        
        print("\nSorted Processes:")
        for process in sorted_processes:
            print(process)

if __name__ == "__main__":
    main()