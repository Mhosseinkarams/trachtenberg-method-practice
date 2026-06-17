import flet as ft

def main(page: ft.Page):
    page.add(ft.Text("Hello, Flet!"))
    # Test Button
    try:
        btn = ft.Button("Test Button")
        page.add(btn)
        print("ft.Button with text created successfully")
    except Exception as e:
        print(f"ft.Button failed: {e}")

    # Test ElevatedButton
    try:
        ebtn = ft.ElevatedButton("Test ElevatedButton")
        page.add(ebtn)
        print("ft.ElevatedButton created successfully")
    except Exception as e:
        print(f"ft.ElevatedButton failed: {e}")

if __name__ == "__main__":
    try:
        print(f"Flet version: {ft.version.version}")
    except:
        print("Could not get Flet version")

    # Try ft.run
    try:
        print("Testing ft.run(main)...")
        # We don't actually want to start a server and block, so maybe just check if it exists
        if hasattr(ft, "run"):
            print("ft.run exists")
        else:
            print("ft.run does NOT exist")

        if hasattr(ft, "app"):
            print("ft.app exists")
        else:
            print("ft.app does NOT exist")
    except Exception as e:
        print(f"ft.run test failed: {e}")
