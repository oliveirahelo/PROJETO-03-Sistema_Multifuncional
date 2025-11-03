# PROJETO 03 — Sistema Multifuncional
# Autor: Professor Ricardo Rodrigues Lima
# Linguagem: Python 3

def linha():
    print("-" * 50)

# ---------------- Calculadora ----------------
def calculadora():
    linha()
    print("🧮 CALCULADORA")
    linha()
    while True:
        print("[1] Adição")
        print("[2] Subtração")
        print("[3] Multiplicação")
        print("[4] Divisão")
        print("[5] Voltar ao menu principal")

        escolha = input("Escolha a operação: ")

        if escolha == "5":
            break

        try:
            a = float(input("Digite o primeiro número: "))
            b = float(input("Digite o segundo número: "))
        except ValueError:
            print("❌ Valor inválido!")
            continue

        if escolha == "1":
            print(f"Resultado: {a + b}")
        elif escolha == "2":
            print(f"Resultado: {a - b}")
        elif escolha == "3":
            print(f"Resultado: {a * b}")
        elif escolha == "4":
            if b == 0:
                print("⚠️ Divisão por zero não permitida!")
            else:
                print(f"Resultado: {a / b}")
        else:
            print("❌ Operação inválida!")

# ---------------- Agenda ----------------
def agenda():
    contatos = []
    linha()
    print("📱 AGENDA DE CONTATOS")
    linha()
    while True:
        print("[1] Adicionar contato")
        print("[2] Listar contatos")
        print("[3] Remover contato")
        print("[4] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "4":
            break
        elif opcao == "1":
            nome = input("Nome: ").strip()
            telefone = input("Telefone: ").strip()
            contatos.append({"nome": nome, "telefone": telefone})
            print(f"✅ Contato '{nome}' adicionado!")
        elif opcao == "2":
            if not contatos:
                print("📭 Nenhum contato cadastrado.")
            else:
                linha()
                print(f"{'NOME':<25}{'TELEFONE':<15}")
                linha()
                for c in contatos:
                    print(f"{c['nome']:<25}{c['telefone']:<15}")
                linha()
        elif opcao == "3":
            nome_remover = input("Digite o nome do contato a remover: ").strip()
            removido = False
            for c in contatos:
                if c["nome"].lower() == nome_remover.lower():
                    contatos.remove(c)
                    removido = True
                    print(f"🗑️ Contato '{nome_remover}' removido!")
                    break
            if not removido:
                print("❌ Contato não encontrado.")
        else:
            print("❌ Opção inválida!")

# ---------------- Gerador de Relatórios ----------------
def relatorios():
    itens = []
    linha()
    print("📊 GERADOR DE RELATÓRIOS SIMPLES")
    linha()
    while True:
        print("[1] Adicionar item")
        print("[2] Listar relatório")
        print("[3] Voltar ao menu principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "3":
            break
        elif opcao == "1":
            nome = input("Nome do item: ").strip()
            try:
                valor = float(input("Valor do item: "))
                itens.append({"nome": nome, "valor": valor})
                print(f"✅ Item '{nome}' adicionado!")
            except ValueError:
                print("❌ Valor inválido!")
        elif opcao == "2":
            if not itens:
                print("📭 Nenhum item cadastrado.")
            else:
                linha()
                print(f"{'ITEM':<25}{'VALOR (R$)':<15}")
                linha()
                total = 0
                for i in itens:
                    print(f"{i['nome']:<25}{i['valor']:<15.2f}")
                    total += i["valor"]
                linha()
                media = total / len(itens)
                print(f"💰 Total: R${total:.2f}")
                print(f"📊 Média: R${media:.2f}")
                linha()
        else:
            print("❌ Opção inválida!")

# ---------------- Menu Principal ----------------
def main():
    while True:
        linha()
        print("💻 SISTEMA MULTIFUNCIONAL")
        linha()
        print("[1] Calculadora")
        print("[2] Agenda de Contatos")
        print("[3] Gerador de Relatórios")
        print("[4] Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            calculadora()
        elif opcao == "2":
            agenda()
        elif opcao == "3":
            relatorios()
        elif opcao == "4":
            print("✅ Encerrando o sistema. Até a próxima!")
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()