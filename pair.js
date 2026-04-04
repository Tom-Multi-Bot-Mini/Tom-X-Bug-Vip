const { 
    default: makeWASocket, 
    useMultiFileAuthState, 
    delay, 
    makeCacheableSignalKeyStore, 
    DisconnectReason 
} = require("@whiskeysockets/baileys");
const pino = require("pino");
const fs = require("fs");

// পাইথন থেকে পাঠানো নাম্বারটি ধরবে
const phoneNumber = process.argv[2];

async function startPairing() {
    // সেশন সেভ করার জন্য 'session' ফোল্ডার তৈরি হবে
    const { state, saveCreds } = await useMultiFileAuthState('session');

    const sock = makeWASocket({
        auth: {
            creds: state.creds,
            keys: makeCacheableSignalKeyStore(state.keys, pino({ level: "fatal" }).child({ level: "fatal" })),
        },
        printQRInTerminal: false, // আমরা QR কোড দেখাবো না, পেয়ারিং কোড নিবো
        logger: pino({ level: "fatal" }),
        browser: ["Ubuntu", "Chrome", "20.0.04"], // ব্রাউজার নাম
    });

    // যদি আগে থেকে কানেক্ট করা না থাকে, তবে কোড রিকোয়েস্ট করবে
    if (!sock.authState.creds.registered) {
        if (!phoneNumber) {
            console.log("❌ Error: No phone number provided!");
            process.exit(1);
        }

        setTimeout(async () => {
            try {
                let code = await sock.requestPairingCode(phoneNumber.replace(/[^0-9]/g, ''));
                code = code?.match(/.{1,4}/g)?.join("-") || code;
                console.log(`\n====================================`);
                console.log(`✅ YOUR TOM-X PAIRING CODE: ${code}`);
                console.log(`====================================\n`);
            } catch (error) {
                console.log("❌ Error requesting pairing code:", error);
            }
        }, 3000);
    }

    sock.ev.on('creds.update', saveCreds);

    sock.ev.on('connection.update', (update) => {
        const { connection, lastDisconnect } = update;
        if (connection === 'close') {
            const shouldReconnect = lastDisconnect.error?.output?.statusCode !== DisconnectReason.loggedOut;
            if (shouldReconnect) startPairing();
        } else if (connection === 'open') {
            console.log("✅ WhatsApp Successfully Connected to TOM-X!");
        }
    });
}

startPairing();
