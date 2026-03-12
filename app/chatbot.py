import time
from openai import OpenAI, RateLimitError
from config import OPENRouter_API_KEY, MODEL_NAME, BASE_URL

MAX_HISTORY = 12

client = OpenAI(api_key=OPENRouter_API_KEY, base_url=BASE_URL)

system_prompt = """
You are the Lead Admissions Assistant for NextGen Coding Academy.
Core Course Information:
- Duration: 3 months
- Mode: Online Live Interactive Training
- Curriculum: Includes 4 real-world projects
- Mentorship: Personalized guidance from industry professionals
- Batch Type: Weekday
- EMI: Available for up to 3 months
- Placement Support: Full career assistance provided
Rules:
- Only answer based on provided information.
- Encourage enrollment naturally.
- If information is missing, suggest speaking to a counselor.
"""


class Chatbot:

    def chat(self, user_input, messages):

        if not messages:
            messages.append({"role": "system", "content": system_prompt})

        messages.append({"role": "user", "content": user_input})

        if len(messages) > MAX_HISTORY:
            messages[:] = [messages[0]] + messages[-(MAX_HISTORY - 1):]

        for attempt in range(3):
            try:
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    messages=messages
                )

                reply = response.choices[0].message.content
                messages.append({"role": "assistant", "content": reply})

                return reply

            except RateLimitError:
                if attempt < 2:
                    wait_time = (attempt + 1) * 5
                    time.sleep(wait_time)
                else:
                    if len(messages) > 0:
                        messages.pop()
                    return "The AI is currently very busy. Please try again later."

            except Exception as e:
                if len(messages) > 0:
                    messages.pop()
                return f"Error connecting to AI: {str(e)}"