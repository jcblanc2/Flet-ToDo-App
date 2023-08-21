import flet as ft


class TodoApp(ft.UserControl):
    def build(self):
        self.txt_task = ft.TextField(hint_text="Enter task", expand=True)
        self.tasks_colunm = ft.Column()
        self.view_main_colunm = ft.Column(
            width=600,
            controls=[
                ft.Row(
                    controls=[
                        self.txt_task,
                        ft.FloatingActionButton(
                            icon=ft.icons.ADD, on_click=self.add_clicked),
                    ],
                ),
                self.tasks_colunm,
            ],
        )

        return self.view_main_colunm

    def add_clicked(self, e):
        self.tasks_colunm.controls.append(ft.Checkbox(label=self.txt_task.value))
        self.txt_task.value = ""
        self.view_main_colunm.update()


def main(page: ft.Page):
    page.title = "ToDo App"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    todo = TodoApp()

    page.add(todo)


ft.app(target=main)
