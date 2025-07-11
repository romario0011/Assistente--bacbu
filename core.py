import random

def analisar_jogo():
    sugestao = random.choice(["🔴 Vermelho", "🔵 Azul", "⚪ Branco"])
    chance = random.choice(["baixa", "média", "alta", "fortíssima"])
    return f"🎯 Sugestão de cor: {sugestao}\n🔥 Probabilidade: {chance.upper()}"

def verificar_padrao_empate():
    tipo = random.choice(["4x", "6x", "10x", "25x", "88x"])
    cobertura = random.choice(["🔴 Vermelho", "🔵 Azul", "⚪ Branco"])
    return f"⚠️ Possível empate detectado ({tipo})\n🎯 Cor de cobertura sugerida: {cobertura}"

def mensagem_status():
    analise = random.choice(["Zig-zag detectado, evitar apostas agora.",
                             "Mercado favorável para entradas.",
                             "Aguardando padrão mais claro..."])
    return f"📡 Status de mesa: {analise}"
