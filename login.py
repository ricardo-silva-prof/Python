import customtkinter as ctk

# Configurações iniciais do tema
ctk.set_appearance_mode("System")  # Modos: "System" (padrão), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Temas: "blue" (padrão), "green", "dark-blue"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.title("Sistema de Login")
        self.geometry("400x500")
        self.resizable(False, False)

        # Layout de grade
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Frame principal para centralizar os widgets
        self.login_frame = ctk.CTkFrame(self, corner_radius=15)
        self.login_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.login_frame.grid_columnconfigure(0, weight=1)

        # Título
        self.label_titulo = ctk.CTkLabel(self.login_frame, text="Bem-vindo",
                                         font=ctk.CTkFont(size=24, weight="bold"))
        self.label_titulo.grid(row=0, column=0, padx=30, pady=(30, 20))

        # Campo de Usuário
        self.entry_usuario = ctk.CTkEntry(self.login_frame, placeholder_text="Usuário",
                                          width=250, height=40)
        self.entry_usuario.grid(row=1, column=0, padx=30, pady=(0, 15))

        # Campo de Senha
        self.entry_senha = ctk.CTkEntry(self.login_frame, placeholder_text="Senha",
                                        show="*", width=250, height=40)
        self.entry_senha.grid(row=2, column=0, padx=30, pady=(0, 15))

        # Botão de Login
        self.botao_login = ctk.CTkButton(self.login_frame, text="Entrar", command=self.acao_login,
                                         width=250, height=40, font=ctk.CTkFont(size=15, weight="bold"))
        self.botao_login.grid(row=3, column=0, padx=30, pady=(10, 20))

        # Checkbox "Lembrar-me" (Opcional)
        self.checkbox_lembrar = ctk.CTkCheckBox(self.login_frame, text="Lembrar-me")
        self.checkbox_lembrar.grid(row=4, column=0, padx=30, pady=(0, 20))
        
        # Link "Esqueci a senha" (Visual)
        self.label_esqueci_senha = ctk.CTkLabel(self.login_frame, text="Esqueceu a senha?",
                                                font=ctk.CTkFont(size=12, underline=True),
                                                cursor="hand2", text_color=("gray60", "gray80"))
        self.label_esqueci_senha.grid(row=5, column=0, padx=30, pady=(0, 20))


    def acao_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()
        
        # Simulação simples de validação (apenas printando no console por enquanto)
        print(f"Tentativa de login:")
        print(f"Usuário: {usuario}")
        print(f"Senha: {senha}")
        
        if usuario == "admin" and senha == "1234":
            print("Login Sucesso!")
            self.label_titulo.configure(text="Sucesso!", text_color="green")
        else:
            print("Falha no login.")
            self.label_titulo.configure(text="Erro no Login", text_color="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()
