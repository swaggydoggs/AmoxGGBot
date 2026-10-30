
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="AmoxGG Bot")

@app.get("/", response_class=HTMLResponse)
async def dashboard():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AmoxGG Bot</title>
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                background: #080d18;
                color: white;
                font-family: Arial, sans-serif;
            }

            header {
                padding: 25px;
                background: #101a2d;
                border-bottom: 1px solid #233654;
            }

            header h1 {
                margin: 0;
                color: #60a5fa;
                letter-spacing: 2px;
            }

            header p {
                color: #94a3b8;
            }

            main {
                max-width: 1100px;
                margin: 35px auto;
                padding: 20px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
                gap: 18px;
            }

            .card {
                background: #111c30;
                border: 1px solid #263957;
                border-radius: 14px;
                padding: 24px;
            }

            .card h2 {
                font-size: 16px;
                color: #94a3b8;
            }

            .card p {
                font-size: 25px;
                font-weight: bold;
            }

            .section {
                margin-top: 25px;
            }

            .status {
                color: #fbbf24;
            }

            footer {
                text-align: center;
                color: #64748b;
                padding: 30px;
            }
        </style>
    </head>

    <body>
        <header>
            <h1>AMOXGG BOT</h1>
            <p>YouTube Live Management Dashboard</p>
        </header>

        <main>
            <h2>Dashboard Overview</h2>

            <div class="cards">
                <div class="card">
                    <h2>Bot Status</h2>
                    <p class="status">Not Connected</p>
                </div>

                <div class="card">
                    <h2>Custom Commands</h2>
                    <p>0</p>
                </div>

                <div class="card">
                    <h2>Active Timers</h2>
                    <p>0</p>
                </div>

                <div class="card">
                    <h2>YouTube Channel</h2>
                    <p>Not Connected</p>
                </div>
            </div>

            <div class="section card">
                <h2>Welcome to AmoxGG Bot</h2>
                <p>
                    Manage your YouTube livestream commands,
                    timers, moderation and giveaways.
                </p>
                <p class="status">
                    YouTube authorization is not configured yet.
                </p>
            </div>
        </main>

        <footer>
            AmoxGG Bot | YouTube Stream Management
        </footer>
    </body>
    </html>
    """
