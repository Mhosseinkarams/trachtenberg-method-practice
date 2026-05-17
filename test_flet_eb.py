import flet as ft
import asyncio

def test():
    eb = ft.ElevatedButton("Test")
    print(f"ElevatedButton text: {eb.text}")
    print(f"ElevatedButton.focus: {eb.focus}")
    res = eb.focus()
    print(f"ElevatedButton.focus() returned: {res}")
    if asyncio.iscoroutine(res):
        print("It is a coroutine")

if __name__ == "__main__":
    test()
