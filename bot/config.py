import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
selfie_id = os.getenv("SELFIE_ID")
school_id = os.getenv("SCHOOL_ID")
voice_gpt_id = os.getenv("VOICE_GPT_ID")
voice_sql_id = os.getenv("VOICE_SQL_ID")
voice_love_id = os.getenv("VOICE_LOVE_ID")

