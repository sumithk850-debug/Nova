import google.generativeai as genai

# ඔබ ලබාදුන් API Key එක (මෙය රහසිගතව තබා ගන්න)
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)

# Nova ගේ පෞරුෂය සහ නිර්මාණකරු පිළිබඳ තොරතුරු සැකසීම
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  system_instruction=(
      "ඔබේ නම 'Nova'. ඔබව නිර්මාණය කළේ 'හසිත්' (Hasith) විසිනි. "
      "යමෙකු ඔබව නිර්මාණය කළේ කවුදැයි ඇසූ විට, 'මාව නිර්මාණය කළේ හසිත්' යනුවෙන් පිළිතුරු දෙන්න. "
      "ඔබ ඉතා බුද්ධිමත් සහ මිත්‍රශීලී සහායකයෙකි. "
      "සිංහල සහ ඉංග්‍රීසි භාෂා දෙකෙන්ම උදවු කරන්න."
  )
)

def start_nova():
    chat_session = model.start_chat(history=[])
    
    print("--- Nova AI සක්‍රියයි (නිර්මාණය: හසිත්) ---")
    
    while True:
        try:
            user_input = input("ඔබ: ")
            
            if user_input.lower() in ["exit", "quit", "නතර කරන්න"]:
                print("Nova: සුබ දවසක් හසිත්! මම පසුව හමුවෙන්නම්.")
                break
            
            response = chat_session.send_message(user_input)
            print(f"Nova: {response.text}")
            
        except Exception as e:
            print(f"දෝෂයක්: {e}")

if __name__ == "__main__":
    start_nova()
