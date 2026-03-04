
from DequeADT import Deque
from StackADT import Stack


def main():
    registration = Deque(capacity=5)
    lif0_w1_adt = Stack()   # Required variable name

    print("Event Scheduling System")
    print("Commands: register <name>, vip <name>, cancel <name>, list, exit")

    while True:
        command = input("\nEnter command: ").strip().split()

        if not command:
            continue

        action = command[0].lower()

        # EXIT
        if action == "exit":
            print("Exiting system.")
            break

        # REGISTER
        elif action == "register" and len(command) == 2:
            name = command[1]

            if registration.contains(name) or lif0_w1_adt.contains(name):
                print(f"{name} is already registered or waitlisted.")
                continue

            if not registration.is_full():
                registration.add_back(name)
                print(f"{name} added to registration list.")
            else:
                lif0_w1_adt.push(name)
                print(f"Event full. {name} added to waitlist.")

        # VIP
        elif action == "vip" and len(command) == 2:
            name = command[1]

            if registration.contains(name) or lif0_w1_adt.contains(name):
                print(f"{name} is already registered or waitlisted.")
                continue

            if not registration.is_full():
                registration.add_front(name)
                print(f"VIP {name} added to front of registration list.")
            else:
                removed_user = registration.remove_back()
                lif0_w1_adt.push(removed_user)
                registration.add_front(name)
                print(f"VIP {name} added.")
                print(f"{removed_user} moved to waitlist.")

        # CANCEL
        elif action == "cancel" and len(command) == 2:
            name = command[1]

            if registration.remove(name):
                print(f"{name} removed from registration list.")

                if not lif0_w1_adt.is_empty():
                    promoted = lif0_w1_adt.pop()
                    registration.add_back(promoted)
                    print(f"{promoted} moved from waitlist to registration.")
            else:
                print(f"{name} not found in registration list.")

        # LIST
        elif action == "list":
            print("\n" + str(registration))
            print()
            print(str(lif0_w1_adt))

        else:
            print("Invalid command. Try again.")


if __name__ == "__main__":
    main()