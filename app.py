import flet as ft

def main(page: ft.Page):     
    page.theme = ft.theme.Theme(color_scheme_seed='green')    
    page.add(ft.Container(width=100, height=100, bgcolor=ft.colors.CYAN_800), ft.Text(value="hello"))
    
    

ft.app(target=main)   