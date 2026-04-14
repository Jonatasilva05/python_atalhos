import os

estrutura = {
    "servicos-4.0": {
        "backend": {
            "api": {
                "auth": {
                    "login.php": "",
                    "register.php": ""
                },
                "servicos": {
                    "listar.php": ""
                },
                "profissionais": {
                    "listar.php": ""
                },
                "agendamentos": {
                    "criar.php": "",
                    "listar.php": "",
                    "status.php": ""
                }
            },
            "config": {
                "conexao.php": "",
                "cors.php": ""
            },
            "models": {
                "Usuario.php": "",
                "Servico.php": "",
                "Agendamento.php": ""
            },
            "database.sql": ""
        },

        "web": {
            "index.html": "",
            "login.html": "",
            "register.html": "",
            "profissionais.html": "",
            "agendar.html": "",
            "dashboard.html": "",

            "css": {
                "style.css": ""
            },

            "js": {
                "api.js": "",
                "auth.js": "",
                "servicos.js": "",
                "profissionais.js": "",
                "agendamento.js": ""
            },

            "assets": {
                "imagens": {}
            }
        },

        "mobile": {
            "App.tsx": "",
            "app.json": "",
            "package.json": "",

            "src": {
                "screens": {
                    "LoginScreen.tsx": "",
                    "HomeScreen.tsx": "",
                    "ProfissionaisScreen.tsx": "",
                    "AgendamentoScreen.tsx": "",
                    "DashboardScreen.tsx": ""
                },

                "components": {
                    "CardServico.tsx": "",
                    "CardProfissional.tsx": ""
                },

                "services": {
                    "api.ts": ""
                },

                "context": {
                    "AuthContext.tsx": ""
                },

                "styles": {
                    "theme.ts": ""
                }
            }
        },

        "README.md": "# Projeto Serviços 4.0\n",
        ".gitignore": "node_modules/\n.env\n"
    }
}


def criar_estrutura(base, estrutura):
    for nome, conteudo in estrutura.items():
        caminho = os.path.join(base, nome)

        # Se for arquivo (conteúdo é string)
        if isinstance(conteudo, str):
            pasta = os.path.dirname(caminho)
            if pasta:
                os.makedirs(pasta, exist_ok=True)

            with open(caminho, "w", encoding="utf-8") as f:
                f.write(conteudo)

            print(f"📄 Arquivo criado: {caminho}")

        # Se for pasta (conteúdo é dict)
        elif isinstance(conteudo, dict):
            os.makedirs(caminho, exist_ok=True)
            print(f"📁 Pasta criada: {caminho}")

            criar_estrutura(caminho, conteudo)


# EXECUTAR
criar_estrutura(".", estrutura)