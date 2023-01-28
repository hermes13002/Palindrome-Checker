'''
word = input('Word: ')
palindrome = word[::-1]
if word == palindrome:
    print('Correct', palindrome)
else:
    print('Incorrect', palindrome)
'''




import flet as ft

def main(page):
    page.title = "Palindrome Checker"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def window_event(e):
        if e.data == "close":
            page.dialog = confirm_dialog
            confirm_dialog.open = True
            page.update()

    page.window_prevent_close = True
    page.on_window_event = window_event

    def yes_click(e):
        page.window_destroy()

    def no_click(e):
        confirm_dialog.open = False
        page.update()

    confirm_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to exit this app?"),
        actions=[
            ft.ElevatedButton("Yes", on_click=yes_click),
            ft.OutlinedButton("No", on_click=no_click),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def palindrome(e):
        palin.value = word.value[::-1]
        
        if word.value == palin.value:
            page.add(ft.Text(f"Your word is a Palindrome, {palin.value}"))
        else:
            page.add(ft.Text(f"Your word is not a Palindrome, {palin.value}"))

    

    word = ft.TextField(label="Enter your word", width=200)
    palin = ft.Text(value="")

    page.add(
        ft.Row(controls = [word, ft.ElevatedButton("CHECK", on_click=palindrome)],
        alignment=ft.MainAxisAlignment.CENTER,
        )   
    )


ft.app(target=main)