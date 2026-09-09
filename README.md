# AgriDrone Connect

Flask application for booking agricultural drone services.

## Local setup

1. Create and activate a Python virtual environment.
2. Install dependencies with `pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and fill in the values.
4. Start the app with `python app.py`.

## Required environment variables

`SECRET_KEY`, `MONGO_URI`, `ADMIN_USERNAME`, and `ADMIN_PASSWORD_HASH` are required. Generate an admin password hash with:

```powershell
python -c "from werkzeug.security import generate_password_hash; print(generate_password_hash('replace-with-a-strong-password'))"
```

Never commit `.env`, database files, uploaded identity documents, or other personal data.

## Vercel deployment

Import the GitHub repository into Vercel and add the required environment variables in the Vercel project settings for the Production environment. The MongoDB Atlas network access rules must allow Vercel to connect. Vercel storage is ephemeral, so uploaded files should be moved to object storage before production use.