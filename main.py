from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from core import analisar_jogo, verificar_padrao_empate, mensagem_status
from utils import gerar_relatorio, mensagem_motivacional, verificar_meta_diaria

TOKEN = "7703748582:AAE_89xbYfSPMIluT6I8DEhQ-0Tx3wxAwY0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(mensagem_motivacional())

async def analisar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    analise = analisar_jogo()
    await update.message.reply_text(analise)

async def empate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    resultado = verificar_padrao_empate()
    await update.message.reply_text(resultado)

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status = mensagem_status()
    await update.message.reply_text(status)

async def relatorio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    rel = gerar_relatorio()
    await update.message.reply_text(rel)

async def meta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    meta = verificar_meta_diaria(150, 250)
    await update.message.reply_text(meta)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("analisar", analisar))
    app.add_handler(CommandHandler("empate", empate))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("relatorio", relatorio))
    app.add_handler(CommandHandler("meta", meta))
    app.run_polling()
