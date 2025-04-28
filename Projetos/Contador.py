import flet as ft

def main(page: ft.Page):
    page.tittle = 'Contador'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.update()
    
if __name__ == '__main__':
    ft.app(target=main)