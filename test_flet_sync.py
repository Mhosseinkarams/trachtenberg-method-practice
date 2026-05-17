import flet as ft
import asyncio

def test():
    tf = ft.TextField()
    print(f"TextField.focus: {tf.focus}")
    res = tf.focus()
    print(f"TextField.focus() returned: {res}")
    if asyncio.iscoroutine(res):
        print("It is a coroutine")
    else:
        print("It is NOT a coroutine")

    btn = ft.Button("Text")
    print(f"Button: {btn}")
    print(f"Button text: {btn.text}")

if __name__ == "__main__":
    test()
