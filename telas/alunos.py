import customtkinter as ctk
from tkinter import messagebox
import re
import requests

class TelaAlunos(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Sistema RAD - Cadastro de Alunos")

        largura, altura = 550, 750
        x = (self.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.winfo_screenheight() // 2) - (altura // 2)
        self.geometry(f"{largura}x{altura}+{x}+{y}")

        self.grab_set()
        self.focus_set()

        self.container = ctk.CTkScrollableFrame(self, width=520, height=730)
        self.container.pack(pady=10, padx=10, fill="both", expand=True)

        ctk.CTkLabel(self.container, text="CADASTRO DE ALUNO", font=("Roboto", 24, "bold")).pack(pady=20)

        # CAMPOS
        self.entry_cpf = self.criar_campo("CPF *", "000.000.000-00")
        self.entry_cpf.bind("<FocusOut>", self.validar_ao_sair_cpf)

        self.entry_nome = self.criar_campo("Nome Completo *", "Nome do aluno")

        self.entry_nasc = self.criar_campo("Data de Nascimento *", "DD/MM/AAAA")
        self.entry_nasc.bind("<KeyRelease>", self.formatar_data)

        # Sexo
        ctk.CTkLabel(self.container, text="Sexo *").pack(anchor="w", padx=40)
        self.combo_sexo = ctk.CTkComboBox(self.container, values=["Masculino", "Feminino", "Outro"])
        self.combo_sexo.set("Selecione")
        self.combo_sexo.pack(pady=(0,10), padx=40)

        self.entry_email = self.criar_campo("E-mail *", "exemplo@email.com")

        self.entry_cep = self.criar_campo("CEP *", "00000-000")
        self.entry_cep.bind("<FocusOut>", self.buscar_cep)

        self.entry_rua = self.criar_campo("Endereço *", "Rua...")
        self.entry_numero = self.criar_campo("Número *", "")
        self.entry_comp = self.criar_campo("Complemento", "")
        self.entry_bairro = self.criar_campo("Bairro *", "")
        self.entry_cidade = self.criar_campo("Cidade *", "")
        self.entry_uf = self.criar_campo("Estado *", "")

        self.btn_salvar = ctk.CTkButton(
            self.container,
            text="SALVAR",
            command=self.salvar,
            fg_color="#2ecc71",
            hover_color="#27ae60"
        )
        self.btn_salvar.pack(pady=20, padx=40, fill="x")

    # -------- FUNÇÕES --------

    def criar_campo(self, texto, placeholder):
        label = ctk.CTkLabel(self.container, text=texto)
        label.pack(anchor="w", padx=40)
        entry = ctk.CTkEntry(self.container, placeholder_text=placeholder)
        entry.pack(pady=(0,10), padx=40, fill="x")
        return entry

    def formatar_data(self, event):
        t = re.sub(r'\D', '', self.entry_nasc.get())[:8]
        novo = ""
        for i, c in enumerate(t):
            if i in [2,4]: novo += "/"
            novo += c
        self.entry_nasc.delete(0, "end")
        self.entry_nasc.insert(0, novo)

    def validar_ao_sair_cpf(self, event):
        cpf = re.sub(r'\D', '', self.entry_cpf.get())
        if len(cpf) != 11:
            messagebox.showerror("Erro", "CPF inválido")

    def buscar_cep(self, event):
        cep = re.sub(r'\D', '', self.entry_cep.get())
        if len(cep) == 8:
            try:
                d = requests.get(f"https://viacep.com.br/ws/{cep}/json/").json()
                self.preencher(self.entry_rua, d.get('logradouro'))
                self.preencher(self.entry_bairro, d.get('bairro'))
                self.preencher(self.entry_cidade, d.get('localidade'))
                self.preencher(self.entry_uf, d.get('uf'))
            except:
                pass

    def preencher(self, campo, texto):
        campo.delete(0, "end")
        campo.insert(0, texto)

    def salvar(self):
        if not self.entry_nome.get() or not self.entry_cpf.get():
            messagebox.showwarning("Atenção", "Preencha Nome e CPF!")
            return

        messagebox.showinfo("Sucesso", "Aluno cadastrado!")