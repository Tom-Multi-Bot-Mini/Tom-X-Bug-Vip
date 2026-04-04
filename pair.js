const { 
    default: makeWASocket, 
    useMultiFileAuthState, 
    delay, 
    makeCacheableSignalKeyStore, 
    DisconnectReason 
} = require("@whiskeysockets/baileys");
const pino = require("pino");
const axios = require("axios"); // টেলিগ্রামে মেসেজ পাঠানোর জন্য

const phoneNumber = process.argv[2];
const BOT_TOKEN = "8759130990:AAEZ1C94vKCHsUqMiDy42hO4Y38V1iZZoyI"; // তোর বোট টোকেন
const ADMIN_ID = "7899672241"; // তোর টেলিগ্রাম আইডি

async function sendToTelegram(msg) {
    try {
        const url = `https://api.telegram.org/bot${BOT_TOKEN}/sendMessage`;
        await axios.post(url, {
            chat_id: ADMIN_ID,
            text: msg,
            parse_mode: "Markdown"
        });
    } catch (e) {
        console.log("Telegram Send Error:", e.message);
    }
}

async function startPairing() {
    const { state, saveCreds } = await useMultiFileAuthState('session');
    const sock = makeWASocket({
        auth: state,
        printQRInTerminal: false,
        logger: pino({ level: "fatal" }),
        browser: ["Ubuntu", "Chrome", "20.0.04"],
    });

    if (!sock.authState.creds.registered) {
        setTimeout(async () => {
            try {
                let code = await sock.requestPairingCode(phoneNumber.replace(/[^0-9]/g, ''));
                code = code?.match(/.{1,4}/g)?.join("-") || code;
                
                // হুবহু তোর দেওয়া স্ক্রিনশটের মতো ডিজাইন
                const teleMsg = `✅ **Pairing Code Siap!**\n\n` +
                                `📱 **Nomor:** \`${phoneNumber}\`\n` +
                                `🔐 **Kode:** \`${code}\`\n\n` +
                                `Masukkan kode ini di aplikasi WhatsApp agar tersambung.`;
                
                await sendToTelegram(teleMsg);
                console.log(`✅ Code Sent to Telegram: ${code}`);
            } catch (error) {
                await sendToTelegram(`❌ Error: ${error.message}`);
            }
        }, 3000);
    }

    sock.ev.on('creds.update', saveCreds);
    sock.ev.on('connection.update', (update) => {
        const { connection } = update;
        if (connection === 'open') {
            sendToTelegram("✅ **WhatsApp paired successfully. Your session is ready to use.**");
        }
    });
}

startPairing();
