from controller import get_controllers, read_input
import asyncio

def main():
    print("Hello from ess-corrector!")
    get_controllers()
    asyncio.run(read_input())


if __name__ == "__main__":
    main()
