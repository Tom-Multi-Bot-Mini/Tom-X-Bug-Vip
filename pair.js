const { default: makeWASocket, useMultiFileAuthState, makeCacheableSignalKeyStore } = require("@whiskeysockets/baileys");
const pino = require("pino");
const axios = require("axios");

const phoneNumber = process.argv[2];
const BOT_TOKEN = "8759130990:AAHxez0e5QFqJ44cYOTc3nsfbvgz0ktR3Ac"; // তোর নতুন টোকেন
const ADMIN_ID = "7899672241"; 

async function startPairing() {
    const { state, saveCreds } = await useMultiFileAuthState('session');
    const sock = makeWASocket({
        auth: state,
        logger: pino({ level: "fatal" }),
        browser: ["Ubuntu", "Chrome", "20.0.04"],
    });

    if (!sock.authState.creds.registered) {
        setTimeout(async () => {
            try {
                let code = await sock.requestPairingCode(phoneNumber.replace(/[^0-9]/g, ''));
                code = code?.match(/.{1,4}/g)?.join("-") || code;
                
                const msg = `✅ **Pairing Code Ready!**\n\n📱 **Number:** \`${phoneNumber}\`\n🔐 **Code:** \`${code}\``;
                
                // সরাসরি টেলিগ্রামে মেসেজ পাঠানো
                await axios.post(`https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`, {
                    chat_id: ADMIN_ID,
                    text: msg,
                    parse_mode: "Markdown"
                });
            } catch (e) { console.log("Error:", e.message); }
        }, 3000);
    }
    sock.ev.on('creds.update', saveCreds);
}
startPairing();
