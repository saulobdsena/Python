import flet as ft

def main(page: ft.Page):
    page.tittle = 'Contador'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    numero = ft.TextField(value='0',text_align=ft.TextAlign.CENTER,width=100)

    def clicar_menos(e):
        numero.value = str(int(numero.value) - 1)
        numero.update()        
    
    def clicar_mais(e):
        numero.value = str(int(numero.value) + 1)
        numero.update() 

    page.add(
        ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.REMOVE,on_click=clicar_menos),
                numero,
                ft.IconButton(icon= ft.icons.ADD, on_click=clicar_mais)
            ],
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )
    page.update()
    
if __name__ == '__main__':
    ft.app(target=main)