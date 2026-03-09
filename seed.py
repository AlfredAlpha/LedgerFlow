from faker import Faker
import random
from app import create_app, db
from app.models import Cliente, Colaborador, Mensalidade

fake = Faker("pt_BR")
app = create_app()

with app.app_context():
    print("Criando dados fictícios...")
    db.drop_all()
    db.create_all()

    cargos = ["Contador", "Analista Fiscal", "Financeiro", "Administrador", "Atendimento", "Assistente", "Gestor"]

    for i in range(7):
        colab = Colaborador(
            nome=fake.name(),
            email=f"user{i}@novaconta.com.br",
            senha="123456",
            cargo=random.choice(cargos)
        )
        db.session.add(colab)

    for _ in range(200):
        cliente = Cliente(
            nome=fake.name(),
            empresa=fake.company(),
            cidade="São Paulo",
            email=fake.email(),
            telefone=fake.phone_number(),
            documento=fake.cpf()
        )
        db.session.add(cliente)
        db.session.flush()

        for _ in range(random.randint(1, 4)):
            mensalidade = Mensalidade(
                cliente_id=cliente.id,
                descricao=random.choice(["Mensalidade contábil", "Serviço fiscal", "Assessoria tributária", "Honorários mensais"]),
                valor=random.randint(200, 1200),
                vencimento=f"2026-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
                status=random.choice(["Pago", "Pendente", "Atrasado"]),
                codigo_boleto=f"34191.79001 {random.randint(10000,99999)}.{random.randint(100000,999999)}"
            )
            db.session.add(mensalidade)

    db.session.commit()
    print("Banco populado com sucesso.")
    print("Login: user0@novaconta.com.br | Senha: 123456")
