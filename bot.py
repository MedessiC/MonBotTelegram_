from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Ton token
TOKEN = "7637246376:AAGJ-cyNQzvxHY-CEInesWpNa569_LniEIo"

# Boutons sous la barre de saisie
keyboard = [
    ["💡 Qui suis-je ?", "📌 Services"],
    ["📅 Rendez-vous", "📚 Ebook"],
    ["📞 Contact", "💬 Témoignages"]
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Présentation captivante du bot
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "👋 ** Bienvenue sur mon assistant pro !\n\n"
        "🔥 Je suis un expert en **automatisation & développement **.\n"
        "💡 Mon objectif ? Vous aider à **optimiser votre travail ** avec la technologie.\n\n"
        "📌 Découvrez mes services et contactez-moi 👇",
        reply_markup=reply_markup
    )

# Présentation détaillée
async def qui_suis_je(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "👨‍💻 **À propos de moi** :\n"
        "🔹 Passionné par l'**intelligence artificielle & l'automatisation**.\n"
        "🔹 Expert en **Python, machine learning, et automatisation**.\n"
        "🔹 J'aide les entreprises et particuliers à **gagner du temps & booster leur productivité**.\n\n"
        "📌 **Cliquez sur un bouton ci-dessous** pour en savoir plus !"
    )

# Présentation des services
async def services(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📌 **Mes services :**\n"
        "✅ Développement de **chatbots & assistants virtuels**\n"
        "✅ Automatisation de tâches avec **Python**\n"
        "✅ Scraping & extraction de données\n"
        "✅ Conseil en technologie & IA\n\n"
        "📅 **Prenez rendez-vous** pour discuter de vos besoins !"
    )

# Prendre un rendez-vous
async def rendezvous(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📅 **Prendre un rendez-vous :**\n"
        "🔹 Contactez-moi directement via **Telegram** ou **email**.\n"
        "🔹 Discutons de votre projet et trouvons **une solution adaptée** !\n"
        "📞 Cliquez sur **Contact** pour plus d’infos."
    )

# Télécharger un ebook
async def ebook(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📚 **Ebook du mois :**\n"
        "📖 [Téléchargez ici](https://drive.google.com/file/d/1W7ienO1NqaTtIwmBnPtU38_f_ox2BfaE/view?usp=drive_link)\n\n"
        "🔥 Découvrez mes **ressources exclusives** pour booster votre carrière tech. Apprenez à programmer en Python !"
    )

# Informations de contact
async def contact(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "📞 **Me contacter :**\n"
        "💬 Telegram : @medessi19\n"
        "📧 Email : vivotinc@gmail.com.com\n"
        "🌍 Github : [ProjetGit ](https://github.com/MedessiC)"
    )

# Témoignages clients
async def temoignages(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "💬 **Témoignages clients :**\n"
        "🗣️ *'Super développeur, il a automatisé toutes mes tâches !'* - Client A\n"
        "🗣️ *'Son chatbot m'a fait gagner du temps et de l'argent !'* - Client B\n\n"
        "📌 **Envie d’un projet ? Contactez-moi !**"
    )

# Gérer les réponses aux boutons
async def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == "💡 Qui suis-je ?":
        await qui_suis_je(update, context)
    elif text == "📌 Services":
        await services(update, context)
    elif text == "📅 Rendez-vous":
        await rendezvous(update, context)
    elif text == "📚 Ebook":
        await ebook(update, context)
    elif text == "📞 Contact":
        await contact(update, context)
    elif text == "💬 Témoignages":
        await temoignages(update, context)
    else:
        await update.message.reply_text("❌ Commande non reconnue. Utilisez un bouton.")

# Fonction principale
def main():
    app = Application.builder().token(TOKEN).build()

    # Ajout des commandes
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot Telegram en ligne...")
    app.run_polling()

if __name__ == "__main__":
    main()
