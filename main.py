import flet as ft

def main(page: ft.Page):
    def add_clicked(e):
        tasks_view.controls.append(ft.Text(value=txt_task.value))
        txt_task.value = ""
        view.update()

    txt_task = ft.TextField(hint_text="Enter new task", expand=True)
    btn_add = ft.FloatingActionButton(icon=ft.icons.ADD, on_click=add_clicked)
    tasks_view = ft.Column()
    view = ft.Column(
        width=600,
        controls=[
            ft.Row(
                controls=[
                    txt_task,
                    btn_add
                ],
            ),
            tasks_view,
        ],
    )

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(view)

ft.app(target=main)
