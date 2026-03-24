import customtkinter as ctk

# Importa suas telas
from telas.alunos import TelaAlunos
# (Se tiver depois: professores, disciplinas...)
# from telas.professores import TelaProfessores

# Configuração visual padrão
ctk.set_appearance_mode("light")  # "dark" ou "light"
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema Acadêmico")
        self.geometry("900x600")

        # Centralizar tela
        largura, altura = 900, 600
        x = (self.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura // 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")

        # Título
        ctk.CTkLabel(self, text="SISTEMA ACADÊMICO", 
                     font=("Roboto", 28, "bold")).pack(pady=40)

        # Botões principais (menu simples estilo RAD)
        ctk.CTkButton(self, text="Cadastro de Alunos",
                      command=self.abrir_alunos,
                      width=250, height=50).pack(pady=10)

        # Pode adicionar depois:
        # ctk.CTkButton(self, text="Cadastro de Professores",
        #               command=self.abrir_professores).pack(pady=10)

        ctk.CTkButton(self, text="Sair",
                      command=self.quit,
                      fg_color="red",
                      hover_color="#c0392b",
                      width=250, height=50).pack(pady=30)

    # -------- FUNÇÕES --------

    def abrir_alunos(self):
        TelaAlunos(self)

    # def abrir_professores(self):
    #     TelaProfessores(self)


# -------- EXECUÇÃO --------

if __name__ == "__main__":
    app = App()
    app.mainloop()