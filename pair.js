const { default: makeWASocket, useMultiFileAuthState, makeCacheableSignalKeyStore, DisconnectReason } = require("@whiskeysockets/baileys");
const pino = require("pino");
const axios = require("axios");

const phoneNumber = process.argv[2];
const BOT_TOKEN = "8759130990:AAEZ1C94vKCHsUqMiDy42hO4Y38V1iZZoyI";
const ADMIN_ID = "7899672241";

async function sendToTelegram(msg) {
    try {
        await axios.post(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
            chat_id: ADMIN_ID,
            text: msg,
            parse_mode: "Markdown"
        });
    } catch (e) { console.log("Tele Error:", e.message); }
}

async function startPairing() {
    const { state, saveCreds } = await useMultiFileAuthState('session');
    const sock = makeWASocket({
        auth: { creds: state.creds, keys: makeCacheableSignalKeyStore(state.keys, pino({ level: "fatal" })) },
        logger: pino({ level: "fatal" }),
        browser: ["Ubuntu", "Chrome", "20.0.04"],
    });

    if (!sock.authState.creds.registered) {
        setTimeout(async () => {
            try {
                let code = await sock.requestPairingCode(phoneNumber.replace(/[^0-9]/g, ''));
                code = code?.match(/.{1,4}/g)?.join("-") || code;
                const teleMsg = `✅ **Pairing Code Siap!**\n\n📱 **Nomor:** \`${phoneNumber}\`\n🔐 **Kode:** \`${code}\`\n\nMasukkan kode ini di WhatsApp.`;
                await sendToTelegram(teleMsg);
            } catch (error) { await sendToTelegram(`❌ Error: ${error.message}`); }
        }, 3000);
    }
    sock.ev.on('creds.update', saveCreds);
}
startPairing();
