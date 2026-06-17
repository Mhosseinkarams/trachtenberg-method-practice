import flet as ft
import asyncio

async def test():
    page = ft.Page(None, "")
    try:
        btn = ft.Button("Text")
        print("ft.Button('Text') created")
    except Exception as e:
        print(f"ft.Button('Text') failed: {e}")

    tf = ft.TextField()
    if asyncio.iscoroutinefunction(tf.focus) or asyncio.iscoroutine(tf.focus):
        print("TextField.focus is a coroutine")
    else:
        # Check if it returns a coroutine when called
        res = tf.focus()
        if asyncio.iscoroutine(res):
            print("TextField.focus() returned a coroutine")
            await res
        else:
            print("TextField.focus() is synchronous")

if __name__ == "__main__":
    asyncio.run(test())
