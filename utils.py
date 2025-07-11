from datetime import datetime

def mensagem_motivacional():
    frases = [
        "🚀 Hoje é dia de vitória. Confie no processo!",
        "💰 Foque na estratégia, não na emoção.",
        "🔥 Cada rodada é uma chance nova.",
        "🎯 A consistência vence a sorte."
    ]
    from random import choice
    return choice(frases)

def gerar_relatorio():
    return "📊 Lucro do dia: R$ 150\n📈 Semana: R$ 740\n📅 Mês: R$ 3.120\nMeta: Atingida ✅"

def verificar_meta_diaria(banca_inicial, banca_atual):
    lucro = banca_atual - banca_inicial
    if lucro >= 150:
        return f"✅ Meta diária batida! Lucro: R$ {lucro}"
    else:
        restante = 150 - lucro
        return f"📌 Faltam R$ {restante} para bater a meta de hoje."
